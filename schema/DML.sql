-- Insert Members
INSERT INTO Members (FirstName, LastName, Email, Password, DateOfBirth, Gender, RegistrationDate, Phone) VALUES 
('Jasmine', 'Jello', 'jasmine.jello@example.com', '123456', '2003-06-06', 'Female', '2023-04-01', '647-1234'),
('Lati', 'Loux', 'lati.loux@example.com', '123456', '1945-08-20', 'Male', '2023-04-02', '647-5678');

-- Insert Trainers
INSERT INTO Trainers (FirstName, LastName, Email, Password, Specialization) VALUES 
('Nyx', 'H', 'Nyx.H@example.com', '123456', 'Yoga Instructor'),
('Luca', 'Braska', 'luca.braska@example.com', '123456', 'Personal Trainer');

-- Insert Admin Staff
INSERT INTO Admin_Staff (Name, Email, Password, Role) VALUES 
('Vawaz Admin', 'vawaz.admin@example.com', '123456', 'Club Manager');

-- Insert Rooms
INSERT INTO Rooms (RoomName, Capacity) VALUES 
('Yoga Studio', 15),
('Weights Room', 10),
('Cardio Room', 10);

-- Insert Classes
INSERT INTO Classes (ClassName, RoomID, Schedule, TrainerID, DayOfWeek, StartTime, Duration) VALUES 
('Morning Yoga', 1, '2024-04-15 08:00:00', 3, 'Wednesday', '08:00', 60),
('Evening Weight Training', 2, '2024-04-15 18:00:00', 4, 'Wednesday', '18:00', 90),
('Pilates', 3, '2024-04-15 07:00:00', 4, 'Wednesday', '07:00', 45);

-- Insert Room Bookings
INSERT INTO Room_Booking (RoomID, BookingTime, StaffID) VALUES 
(1, '2024-04-15 08:00:00', 5),
(2, '2024-04-15 18:00:00', 5),
(3, '2024-04-15 07:00:00', 5);

-- Insert Personal Training Sessions
INSERT INTO Personal_Training_Sessions (MemberID, TrainerID, StartTime, Duration, DayOfWeek, Status) VALUES 
(1, 4, '2024-04-16 10:00:00', 60, 'Thursday', 'Scheduled'),
(2, 3, '2024-04-17 14:00:00', 60, 'Friday', 'Scheduled');

-- Insert Equipment
INSERT INTO Equipment (EquipmentName, LastMaintenanceDate, NextMaintenanceDate) VALUES 
('Treadmill', '2023-12-01', '2024-06-01'),
('Dumbbells', '2023-11-01', '2024-05-01'),
('Elliptical Machine', '2023-10-01', '2024-04-01');

-- Insert Payments
INSERT INTO Payments (MemberID, Amount, PaymentDate, PaymentType, Status) VALUES 
(1, 100.00, '2024-04-01 09:00:00', 'Credit Card', 'Completed'),
(2, 150.00, '2024-04-02 09:15:00', 'Debit Card', 'Completed');

-- Insert Health Metrics
INSERT INTO Health_Metrics (MemberID, DateRecorded, Height, Weight, BMI, HeartRate, MuscleMass) VALUES 
(1, '2024-04-01', 170, 150, 25, 70, 60),
(2, '2024-04-02', 180, 125, 19, 65, 20);

-- Insert Fitness Goals
INSERT INTO Fitness_Goals (MemberID, Description, GoalWeight, CaloriesBurnt, Deadline, Status) VALUES 
(1, 'Wanting to get shredded', 200, 5500, '2024-12-31', 'In Progress'),
(2, 'Trying to be more flexible and gain weight, preferably muscle mass', 160, 2100, '2024-12-31', 'In Progress');

-- Insert Trainer Availability
INSERT INTO Trainer_Availability (TrainerID, StartTime, EndTime, DayOfWeek) VALUES 
(3, '08:00:00', '12:00:00', 'Monday'),
(3, '14:00:00', '18:00:00', 'Monday'),
(4, '09:00:00', '12:00:00', 'Tuesday'),
(4, '13:00:00', '17:00:00', 'Tuesday'),
(3, '08:00:00', '12:00:00', 'Wednesday'),
(3, '14:00:00', '18:00:00', 'Wednesday'),
(4, '10:00:00', '14:00:00', 'Thursday'),
(4, '15:00:00', '19:00:00', 'Thursday'),
(3, '08:00:00', '12:00:00', 'Friday'),
(3, '14:00:00', '18:00:00', 'Friday'),
(4, '09:00:00', '13:00:00', 'Saturday'),
(4, '14:00:00', '18:00:00', 'Saturday');