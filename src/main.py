import psycopg2

# Connection string. Make sure to update it with your credentials. 

def connect_db():
    try:
        conn = psycopg2.connect(
            database="COMP3005Project",
            user="postgres",
            password="postgres",
            host="localhost",
            port='5432'
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error trying to connect:", error)
        return None

# Function to register member
def register_member(first_name, last_name, email, password, address, phone):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """INSERT INTO Member (FirstName, LastName, Email, Password, Address, Phone)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (first_name, last_name, email, password, address, phone))
        conn.commit()
        print("Member registered successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while registering member:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Get function
def list_member():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM Member"""
        cursor.execute(sql)
        members = cursor.fetchall()

        return members
    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving members:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Manage member profile
def update_member_profile(member_id, first_name, last_name, email, password, address, phone):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """UPDATE Member
                 SET FirstName = %s, LastName = %s, Email = %s, Password = %s, Address = %s, Phone = %s
                 WHERE MemberID = %s"""
        cursor.execute(sql, (first_name, last_name, email, password, address, phone, member_id))
        conn.commit()
        print("Member profile updated successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating member profile:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Display membership dashboard
def display_member_dashboard(member_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM Member WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        member_data = cursor.fetchone()
        print("Member Dashboard:")
        print("MemberID:", member_data[0])
        print("Name:", member_data[1], member_data[2])
        print("Email:", member_data[3])
        print("Address:", member_data[5])
        print("Phone:", member_data[6])

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying member dashboard:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    return member_data


# Display member's health metrics
def display_health_metrics(member_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM HealthMetrics WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        health_metrics_data = cursor.fetchall()
        if len(health_metrics_data) == 0:
            print("No health metrics found for the member.")
        else:
            print("Health Metrics for MemberID", member_id)
            for row in health_metrics_data:
                print("HealthMetricID:", row[0])
                print("Height:", row[2])
                print("Weight:", row[3])
                print("MuscleMass:", row[4])
                print("BPM:", row[5])
                print("DataDate:", row[6])
                print("----------------------")

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying health metrics:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    return health_metrics_data


# Display fitness goals for member
def display_fitness_goals(member_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM FitnessGoals WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        fitness_goals_data = cursor.fetchall()
        if len(fitness_goals_data) == 0:
            print("No fitness goals found for the member.")
        else:
            print("Fitness Goals for MemberID", member_id)
            for row in fitness_goals_data:
                print("GoalID:", row[0])
                print("Description:", row[2])
                print("Goal Weight:", row[3])
                print("Goal Time:", row[4])
                print("Burned Calories:", row[5])
                print("Total Sets:", row[6])
                print("Total Reps:", row[7])
                print("----------------------")

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying fitness goals:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    return fitness_goals_data


# Insert fitness goal into DB
def insert_fitness_goal(member_id, description, goal_weight, goal_time, burned_calories, total_sets, total_reps):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """INSERT INTO FitnessGoals (MemberID, Description, GoalWeight, GoalTime, BurnedCalories, TotalSets, TotalReps)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, description, goal_weight, goal_time, burned_calories, total_sets, total_reps))
        conn.commit()
        print("Fitness goal inserted successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting fitness goal:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Insert health metric into DB
def insert_health_metric(member_id, height, weight, muscle_mass, bpm, data_date):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """INSERT INTO HealthMetrics (MemberID, Height, Weight, MuscleMass, BPM, DataDate)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, height, weight, muscle_mass, bpm, data_date))
        conn.commit()
        print("Health metric inserted successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting health metric:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Managing member schedule
def schedule_training_session(member_id, trainer_id, start_time, duration):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """INSERT INTO PersonalTrainingSession (MemberID, TrainerID, StartTime, Duration)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, trainer_id, start_time, duration))
        conn.commit()
        print("Training session scheduled successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while scheduling training session:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def get_schedule(member_id, trainer_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT * FROM PersonalTrainingSession 
                 WHERE MemberID = %s AND TrainerID = %s"""
        cursor.execute(sql, (member_id, trainer_id))
        sessions = cursor.fetchall()

        print("Training sessions retrieved successfully!")
        return sessions

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving training sessions:", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


def get_member_personal_session(member_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT pts.*, t.firstname, t.lastname 
                 FROM PersonalTrainingSession pts
                 INNER JOIN Trainer t ON pts.TrainerID = t.TrainerID
                 WHERE pts.MemberID = %s"""
        cursor.execute(sql, (member_id,))
        sessions = cursor.fetchall()

        print(sessions)
        print("Personal training sessions retrieved successfully!")
        return sessions

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving personal training sessions:", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


def get_class_registration(member_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = """SELECT c.*, cr.dateregistration, t.firstname, t.lastname 
                         FROM ClassSchedule c
                         INNER JOIN ClassRegistration cr ON c.ClassID = cr.ClassID
                         INNER JOIN Trainer t ON c.TrainerID = t.TrainerID
                         WHERE cr.MemberID = %s"""
        cursor.execute(sql, (member_id,))
        classes = cursor.fetchall()
        print(classes)

        print("Class registrations retrieved successfully!")
        return classes

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving class registrations:", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


# Trainer Availability
def set_trainer_availability(trainer_id, availabilities):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Deleting availability slots
        sql_delete = """DELETE FROM TrainerAvailability WHERE TrainerID = %s"""
        cursor.execute(sql_delete, (trainer_id,))
        conn.commit()

        # Add new availability slots
        for availability in availabilities:
            start_time, end_time, day_of_week = availability
            sql_insert = """INSERT INTO TrainerAvailability (TrainerID, StartTime, EndTime, DayOfWeek)
                            VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql_insert, (trainer_id, start_time, end_time, day_of_week))
            conn.commit()

        print("Trainer availability set successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while setting trainer availability:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Retrieve trainer info by ID
def get_trainer_info(trainer_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT * FROM Trainer WHERE TrainerID = %s"""
            cursor.execute(sql, (trainer_id,))
            trainer_info = cursor.fetchone()
            return trainer_info
        except psycopg2.Error as e:
            print("Error retrieving trainer information:", e)
        finally:
            if conn:
                conn.close()


# Retrieve trainer availability by ID
def get_trainer_availabilities(trainer_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT * FROM TrainerAvailability WHERE TrainerID = %s"""
            cursor.execute(sql, (trainer_id,))
            availabilities = cursor.fetchall()
            return availabilities
        except psycopg2.Error as e:
            print("Error retrieving trainer availabilities:", e)
        finally:
            if conn:
                conn.close()


def register_for_class(member_id, class_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Check if member is registered already
        sql_check = "SELECT * FROM ClassRegistration WHERE MemberID = %s AND ClassID = %s"
        cursor.execute(sql_check, (member_id, class_id))
        existing_registration = cursor.fetchone()

        if existing_registration:
            print("Member is already registered for this class.")
            return False

        # Insert new registration
        sql_insert = "INSERT INTO ClassRegistration (MemberID, ClassID, DateRegistration) VALUES (%s, %s, CURRENT_DATE)"
        cursor.execute(sql_insert, (member_id, class_id))
        conn.commit()

        print("Registration for class successfully.")
        return True

    except (Exception, psycopg2.Error) as error:
        print("Error registering for class:", error)
        return False

    finally:
        if conn:
            cursor.close()
            conn.close()