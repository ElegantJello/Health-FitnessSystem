-- Create Members Table
CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(50) NOT NULL CHECK (Gender IN ('Male', 'Female', 'Other')),
    RegistrationDate DATE NOT NULL,
    Phone VARCHAR(20)
);

-- Create Health Metrics Table
CREATE TABLE Health_Metrics (
    MetricID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    DateRecorded DATE NOT NULL,
    Height FLOAT NOT NULL,
    Weight FLOAT NOT NULL,
    BMI FLOAT NOT NULL,
    HeartRate INT,
    MuscleMass FLOAT
);

-- Create Fitness Goals Table
CREATE TABLE Fitness_Goals (
    GoalID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    Description TEXT,
    GoalWeight FLOAT,
    CaloriesBurnt INT,
    Deadline DATE,
    Status VARCHAR(100) NOT NULL CHECK (Status IN ('Not Started', 'In Progress', 'Completed', 'Failed'))
);

-- Create Trainers Table
CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Specialization VARCHAR(100) NOT NULL
);

-- Create Trainer Availability Table
CREATE TABLE Trainer_Availability (
    AvailabilityID SERIAL PRIMARY KEY,
    TrainerID INT REFERENCES Trainers(TrainerID),
    StartTime TYPE TIME USING StartTime::TIME, NOT NULL,
    EndTime TYPE TIME USING EndTime::TIME NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL
);

-- Create Admin Staff Table
CREATE TABLE Admin_Staff (
    StaffID SERIAL PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(100) NOT NULL
);

-- Create Rooms Table
CREATE TABLE Rooms (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(100) NOT NULL,
    Capacity INT NOT NULL
);

-- Create Classes Table
CREATE TABLE Classes (
    ClassID SERIAL PRIMARY KEY,
    ClassName VARCHAR(100) NOT NULL,
    RoomID INT REFERENCES Rooms(RoomID),
    Schedule TIMESTAMP NOT NULL,
    TrainerID INT REFERENCES Trainers(TrainerID),
    DayOfWeek VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    Duration INT NOT NULL
);

-- Create Room Booking Table
CREATE TABLE Room_Booking (
    BookingID SERIAL PRIMARY KEY,
    RoomID INT REFERENCES Rooms(RoomID),
    BookingTime TIMESTAMP NOT NULL,
    StaffID INT REFERENCES Admin_Staff(StaffID)
);

-- Create Personal Training Sessions Table
CREATE TABLE Personal_Training_Sessions (
    SessionID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    TrainerID INT REFERENCES Trainers(TrainerID),
    StartTime TIMESTAMP NOT NULL,
    Duration INT NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled'))
);

-- Create Equipment Table
CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(100) NOT NULL,
    LastMaintenanceDate DATE,
    NextMaintenanceDate DATE
);

-- Create Payments Table
CREATE TABLE Payments (
    PaymentID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID),
    Amount DECIMAL(10, 2) NOT NULL CHECK (Amount > 0),
    PaymentDate TIMESTAMP NOT NULL,
    PaymentType VARCHAR(50) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Completed', 'Cancelled'))
);
