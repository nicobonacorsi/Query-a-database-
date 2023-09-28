
import json

def media_studente(stud_code, dbsize):
    
    # Genero il nome del file JSON degli esami basato su dbsize
    exams_filename = f"{dbsize}_exams.json"
    
    # Inizializzo la variabile total_score a zero
    total_score = 0
    
    # Inizializzo il conteggio degli esami a zero
    exam_count = 0
    
    # Apro il file JSON degli esami in modalità di lettura
    with open(exams_filename, 'r',encoding="utf-8") as exams_file:
        exams_data = json.load(exams_file)
    
    # Calcola i voti e il conteggio degli esami per ciascuno studente
    for exam in exams_data:
        if exam["stud_code"] == stud_code:
            total_score += exam["grade"]
            exam_count += 1

    # Calcolo la media dei voti dello studente specifico
    if exam_count > 0:
        media = total_score / exam_count
        media_arrotondata = round(media, 2)
        numero_str = str(media_arrotondata)

        if numero_str.endswith(".0"):
            numero_format = float(numero_str)
        else:
            numero_format = "{:.2f}".format(media_arrotondata)
            numero_format = float(numero_format)

        return numero_format
    else:
        return 0.0
    # Restituisci 0.0 se lo studente non ha esami registrati o non esiste
    


def media_corso(course_code, dbsize):
    
    # Genero il nome del file JSON degli esami basato su dbsize
    exams_filename = f"{dbsize}_exams.json"    
    # Apro il file JSON in modalità di lettura
    
    with open(exams_filename, 'r',encoding="utf-8") as exams_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        exams_data = json.load(exams_file)
        
        # Inizializzo una variabile per la somma dei voti del corso
    somma_voti_corso = 0
       
       # Inizializzo una variabile per il conteggio di voti del corso
    conteggio_voti = 0
    
    # Ciclo attraverso gli esami e accumula i voti per il corso specifico
    for exam in exams_data:
        if exam["course_code"] == course_code:
            somma_voti_corso += exam["grade"]
            conteggio_voti += 1
     # Calcolo la media dei voti
    if conteggio_voti > 0:
        media = somma_voti_corso / conteggio_voti
        media_arrotondata = round(media, 2)
        numero_str = str(media_arrotondata)

        if numero_str.endswith(".0"):
            numero_format = float(numero_str)
        else:
            numero_format = "{:.2f}".format(media_arrotondata)
            numero_format = float(numero_format)

        return numero_format
    else:
        return 0.0  # Nel caso in cui il corso non abbia voti
    
def media_docente(teach_code, dbsize):
    teachers_filename = f"{dbsize}_teachers.json"
    # Genero il nome del file JSON degli studenti basato su dbsize
    courses_filename = f"{dbsize}_courses.json"
    # Genero il nome del file JSON degli esami basato su dbsize
    exams_filename = f"{dbsize}_exams.json"
    # Apro il file JSON in modalità di lettura
    
    with open(teachers_filename, 'r',encoding="utf-8") as teachers_file:
        # Carica i dati dal file JSON e convertili in una struttura di dati Python
    
        teachers_data = json.load(teachers_file)
        
    # Apro il file JSON in modalità di lettura
    
    with open(courses_filename, 'r',encoding="utf-8") as courses_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        courses_data = json.load(courses_file)
    
    # Apro il file JSON in modalità di lettura
    
    with open(exams_filename, 'r') as exams_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        exams_data = json.load(exams_file)
        
     # Inizializzo una variabile per la somma dei voti degli esami tenuti dal docente
    somma_voti = 0
    
    # Inizializzo una variabile per il conteggio dei voti dei corsi tenuti dal docente
    conteggio_corsi = 0
    
     
    # Cerco lo studente nel database degli studenti
    for teacher in teachers_data:
        if teacher["teach_code"] == teach_code:
            for course in courses_data:
                if course["teach_code"] == teach_code:
                    corso=course["course_code"]
                    for exam in exams_data:
                        if exam["course_code"]==corso:
                            somma_voti += exam['grade']
                            conteggio_corsi += 1
                    
     # Calcolo la media dei voti
    if conteggio_corsi > 0:
        media=somma_voti / conteggio_corsi
        media_arrotondata = round(media, 2)
        numero_str = str(media_arrotondata)

        if numero_str.endswith(".0"):
            numero_format = float(numero_str)
        else:
            numero_format = "{:.2f}".format(media_arrotondata)
            numero_format = float(numero_format)

        return numero_format
    else:
        return 0.0  # Nel caso in cui lo studente non abbia esami registrati


def studenti_brillanti(dbsize):
    # Genero il nome del file JSON degli studenti basato su dbsize
    students_filename = f"{dbsize}_students.json"
    
    with open(students_filename, 'r',encoding="utf-8") as students_file:
        # Carica i dati dal file JSON e convertili in una struttura di dati Python
    
        students_data = json.load(students_file)
    
    studenti_media={}

    for student in students_data:
        stud_code = student["stud_code"]
        media = media_studente(stud_code, dbsize)
        studenti_media[stud_code] = media
        
     # Filtro gli studenti brillanti in base alla media
    studenti_brillanti = [student for student in students_data if studenti_media[student["stud_code"]] >= 28]
    
    studenti_brillanti.sort(key=lambda student: (-studenti_media[student["stud_code"]], student["stud_surname"], student["stud_name"],int(student["stud_code"])))
        
    lista_codici=[student["stud_code"] for student in studenti_brillanti]
    
    return lista_codici



def stampa_verbale(exam_code, dbsize, fileout):
    
    exams_filename = f"{dbsize}_exams.json"
    students_filename = f"{dbsize}_students.json"
    courses_filename = f"{dbsize}_courses.json"
    teachers_filename = f"{dbsize}_teachers.json"
    
    with open(exams_filename, 'r',encoding="utf-8") as exams_file:
        exams_data = json.load(exams_file)
    
    with open(students_filename, 'r',encoding="utf-8") as students_file:
        students_data = json.load(students_file)
    
    with open(courses_filename, 'r',encoding="utf-8") as courses_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        courses_data = json.load(courses_file)
    
    with open(teachers_filename, 'r',encoding="utf-8") as teachers_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        teachers_data = json.load(teachers_file)
    
    exam=None
    for e in exams_data:
        if e["exam_code"] == exam_code:
            exam = e
            break
    
    if exam is None:
        return None  # Esame non trovato
    
    # Estraggo le informazioni dall'esame
    codice_studente = exam["stud_code"]
    data_esame = exam["date"]
    codice_corso = exam["course_code"]
    voto_esame = exam["grade"]
                    
    studente = None
    corso = None
    insegnante = None
    
    # Trovo lo studente, il corso e l'insegnante
    for student in students_data:
        if student["stud_code"] == codice_studente:
            studente = student
            break
    
    for course in courses_data:
        if course["course_code"] == codice_corso:
            corso = course
            break
    
    if corso is not None:
        for teacher in teachers_data:
            if teacher["teach_code"] == corso["teach_code"]:
                insegnante = teacher
                break
    
    if studente is None or corso is None or insegnante is None:
        return "Informazioni mancanti"  # Informazioni mancanti
                
    
    # Scrivo le informazioni relative all'esame nel fileout
    with open(fileout, 'w',encoding="utf-8") as output_file:
        output_file.write(f"Lo studente {studente['stud_name']} {studente['stud_surname']}, matricola {codice_studente}, ha sostenuto in data {data_esame} l'esame di {corso['course_name']} con il docente {insegnante['teach_name']} {insegnante['teach_surname']} con votazione {voto_esame}.\n")
        
    return voto_esame


def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    exams_filename = f"{dbsize}_exams.json"
    students_filename = f"{dbsize}_students.json"
    courses_filename = f"{dbsize}_courses.json"
   
    
    with open(exams_filename, 'r',encoding="utf-8") as exams_file:
        exams_data = json.load(exams_file)
    
    with open(students_filename, 'r',encoding="utf-8") as students_file:
        students_data = json.load(students_file)
    
    with open(courses_filename, 'r',encoding="utf-8") as courses_file:
        # Carico i dati dal file JSON e convertili in una struttura di dati Python
    
        courses_data = json.load(courses_file)
          
    # Trovo lo studente specifico
    student = None
    for s in students_data:
        if s["stud_code"] == stud_code:
            student = s
            break
        
    
    if student is None:
        return 0  # Studente non trovato
    
    
    # Estraggo le informazioni dall'esame
    codice_studente = s["stud_code"]
    cognome = s["stud_surname"]
    nome = s["stud_name"]
    

    student_exams = [exam for exam in exams_data if exam["stud_code"] == codice_studente]
    #lista dei codici di corso in ordine di posizione
    course_codes=[exam["course_code"] for exam in student_exams]
    nomi_corsi=[]

    for codice_corso in course_codes:
        for corso in courses_data:
            if corso["course_code"]==codice_corso:
                nomi_corso = corso["course_name"]
                nomi_corsi.append(nomi_corso)
    
    student_exams.sort(key=lambda exam: (exam["date"], nomi_corsi[course_codes.index(exam["course_code"])]))   
    max_course_name_length = max(len(nome_corso) for nome_corso in nomi_corsi)
        
                

   # Scrivo le informazioni relative agli esami nel fileout
    with open(fileout, 'w',encoding="utf-8") as output_file:
        output_file.write(f"Esami sostenuti dallo studente {cognome} {nome}, matricola {codice_studente}\n")
        for exam in student_exams:
            course_code = exam["course_code"]
            course_name = nomi_corsi[course_codes.index(course_code)]
            date = exam["date"]
            grade = exam["grade"]
            output_line = f"{course_name.ljust(max_course_name_length)}\t{date}\t{grade}\n"
            output_file.write(output_line)
            
    return len(student_exams)



def stampa_studenti_brillanti(dbsize, fileout):
    s_brillanti = studenti_brillanti(dbsize)

    students_filename = f"{dbsize}_students.json"


    with open(students_filename, 'r', encoding="utf-8") as students_file:
        students_data = json.load(students_file)

    # Lista dei dati degli studenti con medie
    studenti_con_medie = []
  

    for codice in s_brillanti:
        media_alunno = media_studente(codice, dbsize)

        for student in students_data:
            if student["stud_code"] == codice:
                studenti_con_medie.append((student["stud_surname"], student["stud_name"], media_alunno))
    # Ordino le righe in modo decrescente per media
    studenti_ordinati = sorted(studenti_con_medie,reverse=False, key=lambda x: (-x[2], x[0], x[1]))
    
    
    max_nome_cognome_length = max(len(f"{cognome} {nome}") for cognome, nome, _ in studenti_ordinati)

    num_linee=0
    # Scrivo le informazioni nel fileout
    with open(fileout, 'w', encoding="utf-8") as output_file:
        for cognome, nome, media in studenti_ordinati:
            
            nome_cognome = f"{cognome} {nome}"
            # Formatto la media per avere una larghezza fissa 
            
            formatted_line = f"{nome_cognome:<{max_nome_cognome_length}}\t{media}\n"
            output_file.write(formatted_line)
            num_linee += 1

    return num_linee





