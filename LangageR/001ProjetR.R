verifier_numero <-function(numero) {
  if((nchar(numero) == 7) && (grepl("[[:upper:]][[:digit:]]+", numero))){
    return(TRUE)
  }
  else {
    return(FALSE)
  }
}
verifier_nom<-function(nom){
  if (grepl("^[A-Za-z]", nom) && (sum(grepl("[A-Za-z]", strsplit(nom, "")[[1]])) >= 2)) {
    return (TRUE)
  } else {
    return (FALSE)
  }}
verifier_prenom<-function(prenom){
  if (grepl("^[A-Za-z]", prenom) && (sum(grepl("[A-Za-z]", strsplit(prenom, "")[[1]])) >= 3)) {
    return (TRUE)
  } else {
    return (FALSE)
  }}
verifier_notes <- function(note) {
  devoir_valides <- TRUE
  examen_valide <- TRUE
  note <- gsub("\\,",".",note)
  note <- strsplit(note, " ")
  note <- strsplit(note, "#")
  for (not in note) {
    notes <- strsplit(not, "\\[")[[1]][2]
    print(notes)
    for (no in notes) {
      devoir <- strsplit(no, ":")[[1]][1]
      examen <- strsplit(no, ":")[[1]][2]
      examen <- strsplit(examen, "]")[[1]][1]
      if(all(sapply(examen, function(x) x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")))) {
        examen <- as.numeric(examen)
      } else {
        examen_valide <- FALSE
        break
      } 
      for (note in strsplit(devoir, "\\|")[[1]]) {
        if(all(sapply(note, function(x) x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")))) {
          note <- as.numeric(note)
        } else {
          devoir_valides <- FALSE
          break
        }
        if ((as.numeric(note) < 0||as.numeric(note) > 20)) {
          devoir_valides <- FALSE
          break
        }
      }
      if (!(is.numeric(examen)) || as.numeric(examen) < 0 || as.numeric(examen) > 20) {
        break
        examen_valide <- FALSE
      }
    }
  }
  if (devoir_valides == FALSE && examen_valide == FALSE) {
    return(FALSE)
  } else if (devoir_valides == FALSE && examen_valide == TRUE) {
    return(FALSE)
  } else if (devoir_valides == TRUE && examen_valide == FALSE) {
    return(FALSE)
  } else if (devoir_valides == TRUE && examen_valide == TRUE) {
    return(TRUE)
  }
}
verifier_date <- function(date) {
    bissextile <- FALSE
    date <- gsub("fev", "02", date)
    date <- gsub("mars", "03", date)
    date <- gsub("decembre", "12", date)
    date <- gsub("[[:punct:]]|[[:space:]]", "/", date)
    composantes <- strsplit(date, "/")[[1]]
    jour <- (composantes[1])
    mois <- (composantes[2])
    annee <- (composantes[3])
    annee <- strsplit(annee, "")[[1]]
    mois <- strsplit(mois, "")[[1]]
    jour <- strsplit(jour, "")[[1]]
    if(all(sapply(annee, function(x) x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")))) {
      annee <- as.numeric(composantes[3])
    } else {
      return (FALSE)
    } 
    if(all(sapply(jour, function(x) x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")))) {
      jour <- as.numeric(composantes[1])
    } else {
      return (FALSE)
    }
    if(all(sapply(mois, function(x) x %in% c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")))) {
      mois <- as.numeric(composantes[2])
    } else {
      return (FALSE)
    }
    if ((annee %% 4 == 0 & annee %% 100 != 0) | annee %% 400 == 0) {
      bissextile <- TRUE
    }
    
    mois_valide <- FALSE
    if (mois >= 1 & mois <= 12) {
      mois_valide <- TRUE
    }
    
    jour_valide <- FALSE
    if (mois == 2) {
      if (bissextile & jour >= 1 & jour <= 29) {
        jour_valide <- TRUE
      } else if (!bissextile & jour >= 1 & jour <= 28) {
        jour_valide <- TRUE
      }
    } else if (mois == 4 | mois == 6 | mois == 9 | mois == 11) {
      if (jour >= 1 & jour <= 30) {
        jour_valide <- TRUE
      }
    } else if (mois == 1 | mois == 3 | mois == 5 | mois == 7 | mois == 8 | mois == 10 | mois == 12) {
      if (jour >= 1 & jour <= 31) {
        jour_valide <- TRUE
      }
    }
    
    if (mois_valide & jour_valide) {
      return(TRUE)
    } else {
      return(FALSE)
    }
}
verifier_classe <- function(classe) {
  premier_caractere <- substr(classe, 1, 1)
  dernier_caractere <- substr(classe, nchar(classe), nchar(classe))
  if (premier_caractere %in% c("3", "4", "5", "6") && dernier_caractere %in% c("A", "B")) {
    return(TRUE)
  } else {
    return(FALSE)
  }
}

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
library(readr)
data<- read.csv("Téléchargements/Donnees_Projet_Python_DataC5.csv",sep=",")
#data <- subset(data, !apply(data,1, function(x) any(x == "")))
valid_lines <- data.frame(matrix(ncol = 7, nrow = 0))
invalid_lines <- data.frame(matrix(ncol = 7, nrow = 0))
print(valid_lines)
print(invalid_lines)
for (i in 1:nrow(data)) {
  row <- data[i,]
  nom <- row$Nom
  prenom <- row$Prénom
  numero <- row$Numero
  classe <- row$Classe
  note <- row$Note
  date <- row$Date.de.naissance
  if (!verifier_nom(nom) || !verifier_prenom(prenom)|| !verifier_numero(numero)|| !verifier_classe(classe)||!verifier_date(date)) {
    invalid_lines <- rbind(invalid_lines, row)
    next
  }
  else{
    valid_lines <- rbind(valid_lines,row)
  }
}
View(invalid_lines)
View(valid_lines)
print(nrow(valid_lines))
print(nrow(invalid_lines))