def solution(k, room_number):
    room_dict = {}
    result = []
    for room in room_number:
        if room in room_dict:
            while room != room_dict[room]:
                next_room = room_dict[room]
                room_dict[room] = room_dict[next_room]
                room = next_room
            
            new_room = room+1
            room_dict[room] = new_room
            if new_room+1 in room_dict:
                room_dict[new_room] = new_room+1
            else:
                room_dict[new_room] = new_room
            result.append(new_room)
        else:
            if room-1 in room_dict:
                room_dict[room-1] = room
            if room+1 in room_dict:
                new_next_room = room+1
            else:
                new_next_room = room
            room_dict[room] = new_next_room
            result.append(room)
            
    return result