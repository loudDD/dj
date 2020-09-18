import random

random.randint


def getroomnumber():
    room = []
    time = [i for i in range(24)]
    meeting1 = {"start": 8, "end": 12}
    meeting2 = {"start": 16, "end": 19}
    meeting3 = {"start": 10, "end": 16}
    meetings = [meeting1, meeting2, meeting3]
    for i in range(len(meetings)):
        romnumber = 0
        start = meetings[i]["start"]
        end = meetings[i]['end']
        duration = [i for i in range(start, end + 1)]
        print("the meeting '{}' duration is {} ".format(i + 1, duration))
        # print("use the {} room".format(len(room)))
        if len(duration) != 0 and len(room) == 0:
            room.append(sorted(time))
            print("now we have 1 room")

        while True:
            try:
                for clock in duration:
                    room[romnumber].remove(clock)
                print("remove the meeting time")
                print("the left room time is ", room[romnumber])
                break
            except Exception as e:
                print("the time is in conflict , will use another room")
                romnumber += 1
                room.append(time)
                print("the room are ", room)
                print("the valid time of room {} is : {}".format(romnumber, room[romnumber]))

    print("must use ", len(room))

# print(room)
