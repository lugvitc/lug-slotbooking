### Slot Booking Flask App

- Fork this repository and clone the forked repository.
- open terminal and run **pip install Flask Flask-SQLAlchemy**
- Run the app.py
- By default it is using a mysql database, fill in the credentials for mysql in line number 6 of app.py.
- You can also use a sqlite database.
- To change database, just modify line number 6 in app.py
- When it is executed for the first time, it will automatically create the required tables.
- Login credentials are the records stored in the SlotBookedApplicants table.
  - To login, you must create a record in the above mentioned table. You need to use the value of the regno field and the password will be the value of the Phoneno field.
  - Therefore create a sample record to login.
    - Sample Record Example:
      - name: test
      - regno: 22BCE1111
      - email: example@example.com
      - phoneNo: 1234567890
      - department1: Technical Department - Backend
      - department2: Media Department
      - slot1_status: 
      - slot2_status:
      - slot1:
      - slot2:
    - slot 1 status, slot 2 status , slot 1, slot 2 will be automatically filled when a slot is booked.
    - Now since this person in the sample record was shortlisted for Technical Department - Backend and Media Department also, you need to create a record in both those tables also for this same person.
    - Then you need to add an available slot for both the department in the Slots table.
      - Example Record for Slots table.
        - slot_id: 1
        - slot_num: 1
        - department: Technical Department - Backend
        - slot: September 28 1:00 PM - 2:00 PM
        - seats: 10
        - seats_left: 10
      - The slots you create here, will be displayed when the user is trying to book the slots. 
      - Every time a slot is booked, the seats left for the slot will decrease. Once there is no seat left in a slot, that slot will be no longer displayed in the slot booking page.
      - Make sure you create slots for all the departments an applicant is shortlisted.
      - For example, here our test applicant is shortlisted for Technical Department - Backend and Media Department. So make sure a slot is created for both the departments.
- If you face any issue, you can reach our technical support team at [Linux Club Forums](https://forum.lugvitc.org)
- Once you have made any improvements or modifications, you can create a pull request. 
- Linux Club Technical Team will review it and if it passes the review, it will be merged to main repository.



### Deploy using Docker

- Make the necessary changes to the app.py file.

- Run ``` docker compose up -d ```



**Developed by Rahul Vijayakumar**

- Github profile: [rahulvk007](https://Github.com/rahulvk007)

- Blog: [rahulvk.com](https://www.rahulvk.com)

**Frontend developed by Dhananjay Chauhan**