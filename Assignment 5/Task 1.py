#!/usr/bin/env python3


# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the List of parameters.
# You may introduce private/protected utility methods though.
class Calendar:

    def __init__(self):
        self.events = {}
        self.ueid = 1

    def add_event(self, date_str, start_time, end_time, description):
        if start_time.split(":")[0] > end_time.split(":")[0]:
            raise Exception("ligma")
        if start_time.split(":")[0] == end_time.split(":")[0] and start_time.split(":")[1] > end_time.split(":")[1]:
            raise Exception("ligma")
        else:
            self.events[date_str] = tuple[self.ueid, start_time, end_time, description]
            self.ueid =+ 1

    def get_events(self, date_str):
        if True:
            rtrnls = []
            for event in self.events[date_str]:
                    rtrnls.append(event)
        return rtrnls   #Not sorted, yet


    def delete_event(self, event_id):
        pass
        #for key, value in self.events.items():
        #    if value[0] == event_id:    #why this no worky?
        #        pass




# You can play around with your implementation in the following body.
# The contained statements will be ignored while evaluating your solution.
if __name__ == "__main__":
    cal = Calendar()
    event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))
