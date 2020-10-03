<h1 align="center"><strong>Employees Management</strong></h1>
<h1 align="center"><strong>[PL]</strong></h2>

<h2 align="center">Projekt: „Employees Management” ma na celu wspomóc codzienną prace biurową firmy.</h3>

<h4 align="center">Podczas testowaniu serwisu, możesz stworzyć konto nowego użytkownika lub skorzystać z jednego z tych:</h5>

<p align="center">
Konto z uprawnieniami: <b>Director</b> <br />
log: albert<br />
pass: samsung666<br />
</p>

<p align="center">
 Konto z uprawnieniami: <b>Manager</b> <br />
log: frank<br />
pass: samsung888<br />
</p>

<p align="center">
Konto z uprawnieniami: <b>Standard</b><br />
log: emma<br />
pass: samsung888<br />
 </p>
 
<p align="center">Opis uprawnień znajduję sie na dole tego dokumentu. </p><br />


<br />
<h3>Funkcjonalność serwisu:</h4>
<br />

**1. Czas pracy pracownika:**

- na stronie głównej, po zalogowaniu się przez pracownika zostają wyświetlona 3 okienka, służące do rejestracji czasu rozpoczęcia pracy, zakończenia pracy, oraz aktualny status pracy w danym dniu.
- po wybraniu odpowiedniej ikony i zatwierdzeniu wyboru, start bądź koniec pracy jest zapisywane w bazie danych wraz z adresem IP.
- podczas rejestracji casu pracy, sprawdzane jest czy pracownik wykonuje operację w odpowiedniej kolejności, co uniemożliwia np. rejestracji zakończenia pracy przed zarejestrowaniem jej rozpoczęcia. W przypadku dokonywania operacji w nie odpowiedniej kolejności zostaje wyświetlony komunikat  informujący o prawidłowej kolejności.
- po zarejestrowaniu początku oraz końca pracy w danym dniu wyliczany jest godzinowy czas pracy zaokrąglany do 15 minut.
 
**2. Wyświetlanie oraz generowanie czasów pracy**
- w zakładce worktime pracownik może sprawdzić czasy swojej pracy w wybranym przez siebie przedziale czasu, które zostaną przedstawione w formie tabelki oraz wykresów
-  wygenerowania danego okresu w formie tabeli do pliku pdf.

**3. Pracownik**
- wypełnienie danych osobowych wykonywane jest w zakładace „Your profile” -> „Edit profile”. Wszystkie dane osobowe, dział pracownika, aktualny projekt, tytuł zawodowy oraz numer karty przepustki, który jest generowany losowo podczas rejestracji można zobaczyć w zakładce „your profile” -> Profile overlook 
- zakładka your profile zawiera także stronę „change password” na której można zmienić hasło do konta.
- menu główne -> Sprawdz pracownika pozwala na sprawdzenie danych osobowych dowolnego pracownika
- stworzenie żądania dodania do odpowiedniej grupy dostępu

**4. Wakacje**
- rezerwacja urlopu
- sprawdzanie swojego zarezerwowanego urlopu dla danego miesiąca w postaci tabeli z datami oraz wyświetlenia widoku kalendarza z zaznaczonymi datami urlopu. poniżej zostają wyświetlone wykresy przedstawiające ilość zarezerwowanych dni urlopu w danym miesiącu do całkowitych dni urlopu, oraz ilość zarezerwowanych dni urlopu w całym roku do całkowitych dni urlopu.
- sprawdzanie zarezerwowanych urlopów wszystkich pracowników dla danego miesiąca w postaci widoku kalendarza z zaznaczonym imieniem oraz nazwiskiem pracownika dla każdego dnia urlopu

**5. Lista zadań**
- Na stronie głównej wyświetlana jest aplikacja To do list, która pozwala na zapisywanie, modyfikowanie oraz usuwanie listy swoich obowiązków. Poniżej wyświetlana jest ich całkowita ilość
- Lista użytkownika zapisywana jest w bazie danych

**6.	Panel z wiadomościami (Chatboard)**
- Message board jest chatem w którym wszyscy użytkownicy mogą zamieszczać wiadomości
-wiadomości przetrzymywane są w bazie danych przez 7 dni od daty wysłania po czym ulegają skasowaniu.
- na menu nawigacyjnym przy nazwie message board pokazywania jest liczba, która informuje o ilości nowych wiadomości od momentu ostatniego odwiedzenia zakładki messageboard. Liczba jest zerowana przy każdym wylogowaniu z portalu

**7. Delegacje**
- tworzenie delegacji
- sprawdzanie swoich delegacji dla danego miesiąca, w postaci generowanego kalendarza z naniesionym krajem oraz miastem dla każdego dnia
- sprawdzanie delegacji wszystkich pracowników dla danego miesiąca w postaci kalendarza z naniesionymi pracownikami oraz miejscem ich delegacji dla każdego dnia
- dodawanie/usuwanie pracowników do istniejących delegacji
- usuwanie delegacji

**8. Działy firmy**
- wyświetlanie wszystkich działów firmy wraz z ich pracownikami oraz ich liczbą
- dodawanie, modyfikowanie oraz usuwanie działów firmy, wraz z ich opisem, lokalizacją
- dodawanie oraz usuwanie pracowników z działu
- dodawanie oraz usuwanie dyrektora działu

**9. Projekty**
- dodawanie projektu, zawierającego pola: unikalna nazwa, początkowa oraz końcowa data projektu, główna lokalizacja, firma dla której realizowany jest projekt, data rejestracji projektu, która jest wypełniania automatycznie, pole mówiące czy projekt jest aktywny czy zakończony
- modyfikowanie projektu
- dodawanie oraz usuwanie pracowników z aktywnych projektów
- dodawanie oraz usuwanie team leadera
- przenoszenie projektu do zakończonych
- wyświetlanie wszystkich projektów z podziałem na aktywne i zakończenie waz z ich opisami, pracownikami oraz team leaderem

**10. Restricted functions**
- podglądu wszystkich żądań z możliwością ich wykonania
- dodania bądź usunięcia pracownika z grupy dostępu
- dodania pracownikowi odpowiedniego tytułu zawodowego oraz przypisania branży
- zakończone żądania usuwane po 21 dniach
- sprawdzanie czasu pracy dowolnego pracownika

**11. Pozostałe funkcje**
- wyświetlanie na stronie głównej grafiki z życzeniami, jeśli pracownik w danym dniu ma urodziny
- pokazywanie informacji na stronie głównej, mówiącej o konieczności wypełnienia reszty danych osobowych.

Trzy główne grupy dostępu: 
- **Standard** – nadawana przy rejestracji pracownika automatycznie
- **Manager** – pełne prawa z wyłączenie, tworzenia oraz modyfikacji działów firmy, oraz ich dyrektorów
- **Director** – pełne prawa

Do zakładki „restricted function” dostęp posiadają wyłącznie użytkownicy z grup: „manager”, „director”. W przypadku próby dostępu użytkownika z grupy standard, zawartość zakładki nie zostanie wyświetlona, wyświetlona zostanie informacja o braku dostępu. <br /><br />
W przypadku próby edycji pozostałych zakładek do których użytkownik nie posiada praw, zawartość zostanie wyświetlona, możliwe będzie przejście przez dostępne funkcjonalności, natomiast nie zostaną one wykonane w bazie danych o czym użytkownik zostanie poinformowany komunikatem o braku odpowiednich uprawnień. <br /><br />
Dodawanie uprawnień dla poszczególnych użytkowników możliwe jest tylko w dół hierarchii. Co oznacza, że użytkownicy z grupy „manager” mogą dodać uprawnienie wyłącznie do tej samej grupy.  Użytkownicy z grupy „director” mogą dodać uprawnienie do grup: „manager”, „director”.<br /><br />

<h3 align="center">Użyte technologie:</h3>
<p align="center">HTML, CSS, Bootstrap, Python, Django, Django Rest Framework, JavaScript, ChartJS</p>

<br /><br /><br /><br />
<h1 align="center"><strong>[ENG]</strong></h2>
<h2 align="center">Project: „Employees Management” aims to support the company`s daily office work.</h3>
<br />
<h3>Functionality:</h4>
<br />

**1. Employee working time:**
- on the home page, after logging in by an employee, 3 windows are displayed, used to record the time of starting work, ending work, and the current status of work on a given day.
- after selecting the appropriate icon and confirming the selection, the start or end of work is saved in the database along with the IP address.
- when registering working time, it is checked whether the employee performs the operation in the right order, which makes it impossible, for example, to register the end of work before registering its commencement. If the operation is performed in an incorrect order, a message informing about the correct sequence is displayed.
 - after recording the beginning and end of work on a given day, the hourly working time is rounded up to 15 minutes.
 
**2. Displaying and generating of working time**
- in the worktime tab, the employee can check the times of his work by himself in the time range that they provide in the form of tables and charts
-  generating a given period in the form of a table to a pdf file.

**3. Employee**
- personal data is filled in  the "Your profile" -> "Edit profile" tab. All personal data, employee department, current project, professional title and pass card number, which is randomly generated during registration can be seen in the tab "your profile" -> Profile overlook
- The "your profile" tab also allows you to change your account password
- “Check employee” on main left menu allows to check the personal data of any employee
- creating a request to be added to the appropriate access group

**4. Vacation**
- holiday booking
- checking your booked holiday for a given month in the form of a table with dates and displaying a calendar view with holiday dates marked. graphs below show the number of reserved vacation days in the given month to the total vacation days, and the number of booked vacation days for the whole year to the total vacation days.
- checking the booked holidays of all employees for a given month in the form of a calendar view with the employee's name and surname marked for each day of leave

**5. To do**
- On the main page, the To do list application is displayed, which allows you to save, modify and delete your list of duties. The total number of them is displayed below
- The user list is saved in the database

**6. Messages Panel**
- message board is a chat room where all users can post messages
- messages are kept in the database for 7 days from the date of sending and then they are deleted.
- on the navigation menu, next to the message board name, there is a number that indicates the number of new messages since the last visit to the message board tab. The number is reset every time you log out of the portal

**7. Delegations**
- creating a delegation
- checking your business trips for a given month in the form of a generated calendar with the country and city marked for each day
- checking the delegation of all employees for a given month in the form of a calendar with marked employees and the place of their delegation for each day
- adding / removing employees to existing delegations
- deleting a delegation

**8. Company departments**
- displaying all departments of the company along with their employees and their amount for a given department
- adding, modifying and removing company departments, along with their description and location 
- adding and removing a department director

**9. Projects**
- adding a project with the following fields: unique name, start and end date of the project, main location, company for which the project is implemented, date of registration of the project, which is automatically filled in, a field indicating whether the project is active or completed
- modifying the project
- adding and removing employees from active projects
- adding and removing a team leader
- finishing projects
- displaying all projects with the division for active and finished projects with their descriptions, employees and team leader

**10. Restricted functions**
- displaying all requests with the possibility of their execution
- adding or removing an employee from an access group
- adding the employee an appropriate job title and assigning the industry
- completed requests deleted after 21 days
- checking the working time of any employee

**11. Other functions**
- displaying a graphic with wishes on the home page if the employee has a birthday on a given day
- showing information on the home page saying that the rest of the personal data must be completed.

**Three main access groups**
- **Standard** – automatically granted upon employee registration 
- **Manager** – full rights, excepted creating and modifying  company departments and their directors
- **Director** – full rights

Only users from the groups: "manager", "director" have access to the "restricted function" tab. If an access attempt is made by user from the standard group, the content of the tab will not be displayed, information that access is denied will be displayed. <br /><br />
When user try to edit the remaining tabs to which the user has no rights, the content will be displayed, it will be possible to go through the available functionalities, but they will not be performed in the database, about which the user will be informed about the lack of appropriate permissions. <br /><br />
Adding authorizations for individual users is possible only down the hierarchy. This means that users from the "manager" group can only add permission to the same group. Users from the "director" group can add rights to the groups: "manager", "director". <br /><br />

<h3 align="center">Technologies used:</h3>
<p align="center">HTML, CSS, Bootstrap, Python, Django, Django Rest Framework, JavaScript, ChartJS</p>



