import mysql.connector as mysqlConnector


def get_set_id(weight, reps):
    try:
        cursor.execute(
            f"""
                SELECT lift_set_id
                FROM HempfieldBaseball.LiftSet
                WHERE weight={weight} AND reps={reps}
            """
        )
        lift_set_id = cursor.fetchone()[0]
    except Exception as e:
        print("Invalid Query")
        print(e)
        conn.close()
        exit()

    return lift_set_id


def get_exercise_id(name):
    try:
        cursor.execute(
            f"""
                SELECT lift_type_id
                FROM HempfieldBaseball.LiftType
                WHERE name='{name}'
            """
        )
        lift_type_id = cursor.fetchone()[0]
    except Exception as e:
        print("Invalid Query on Get Exercise Id")
        print(e)
        conn.close()
        exit()

    return lift_type_id


def insert_strength_increment(lift_type_id, lift_set_id, points, adj):
    # print(exercise_id, set_id, points, adj)
    # cursor.reset()
    try:
        cursor.execute(
            f"""
                INSERT INTO HempfieldBaseball.StrengthIncrement
                SET lift_type_id = {lift_type_id},
                    lift_set_id = {lift_set_id},
                    strength_points = {points - adj}
            """
        )
    except Exception as e:
        print("Invalid Query on Insert")
        print(e)
        conn.close()
        exit()
    conn.commit()


conn = mysqlConnector.connect(host='localhost',
                              user='hempfield_baseball_admin',
                              passwd='hempfield')
if conn:
    # print("Connection Successful")
    pass
else:
    print("Connection Failed")
    exit()

print("Seeding Strength Increments. . .")

cursor = conn.cursor(buffered=True)

# Deadlift
exercise_id = get_exercise_id("Deadlift")
weight = 405
reps = 6
points = 1003.0
adj = 0
while weight >= 65:
    while reps >= 3:
        set_id = get_set_id(weight, reps)

        if reps == 3:
            adj = 13

        insert_strength_increment(exercise_id, set_id, points, adj)
        reps -= 1
        points -= 1.5

    weight -= 5
    reps = 6
    points -= 8.5
    adj = 0

# Squat
exercise_id = get_exercise_id("Squat")
weight = 315
reps = 6
points = 1005.0
adj = 0
while weight >= 45:
    while reps >= 3:
        set_id = get_set_id(weight, reps)

        if reps == 3:
            adj = 15.5

        insert_strength_increment(exercise_id, set_id, points, adj)

        reps -= 1
        points -= 2.5
    weight -= 5
    reps = 6
    points -= 8
    adj = 0

# Bench
exercise_id = get_exercise_id("Bench Press")
weight = 225
reps = 6
points = 1010
adj = 0
while weight >= 45:
    while reps >= 3:
        set_id = get_set_id(weight, reps)

        if reps == 3:
            adj = 22

        insert_strength_increment(exercise_id, set_id, points, adj)

        reps -= 1
        points -= 5
    weight -= 5
    reps = 6
    points -= 7
    adj = 0

# Military
exercise_id = get_exercise_id("Military Press")
weight = 135
reps = 6
points = 1018.0
adj = 0
while weight >= 45:
    while reps >= 3:
        set_id = get_set_id(weight, reps)

        if reps == 3:
            adj = 43

        insert_strength_increment(exercise_id, set_id, points, adj)

        reps -= 1
        points -= 9
    weight -= 5
    reps = 6
    points -= 16
    adj = 0

conn.close()

print("Done!")
