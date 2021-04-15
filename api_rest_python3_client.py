import requests,json

def get_list_student():
    receive = requests.get('http://localhost:7000/api/estudiante/')

    if receive.status_code == 200:
        print (receive.json())
        print('\n\n')
    else:
        print("ERROR!\n\n")

def search_a_student():
    ploads = {'matricula':20011136}
    receive = requests.get('http://localhost:7000/api/estudiante/',params=ploads)

    if receive.status_code == 200:
        print (receive.json())
        print('\n\n')
    else:
        print("ERROR!\n\n")

def create_a_student(nombre,matricula,carrera):
    pload = {'nombre':nombre,'matricula':matricula,'carrera':carrera}
    receive = requests.post('http://localhost:7000/api/estudiante/',data = json.dumps(pload))
 
    if receive.status_code == 200:
        print (receive.json())
        print('\n\n')
    else:
        print("ERROR!\n\n")

def delete_a_student(matricula):
    receive = requests.delete('http://localhost:7000/api/estudiante/'+str(matricula))

    if receive.status_code == 200:
        print (receive.json())
        print('\n\n')
    else:
        print("ERROR!\n\n")


if __name__ == '__main__':
    print('***** ALL STUDENTS *****')
    get_list_student()
    print('***** SEARCHING A STUDENT *****')
    search_a_student()
    print('***** CREATING STUDENTS *****')
    create_a_student('Anthony Sakamoto',20161565,'ITT')
    create_a_student('Wendily Rodriguez',20161579,'ITT')
    print('***** STUDENTS AFTER CREATING*****')
    get_list_student()
    print('***** DELETING CREATED STUDENTS *****')
    delete_a_student(20161565)
    delete_a_student(20161579)
    print('***** STUDENTS AFTER DELETING*****')
    get_list_student()
  
