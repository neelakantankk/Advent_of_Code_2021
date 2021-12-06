def main():
    with open('input.txt','r') as infile:
        initial_fish = [int(x) for x in infile.read().strip().split(",")]
    
    timers_and_fish = dict()

    for fish in initial_fish:
        if fish in timers_and_fish.keys():
            timers_and_fish[fish]+=1
        else:
            timers_and_fish[fish] = 1
    
    max_days = 80

    for day in range(1,max_days+1):
        current_timers = list(timers_and_fish.keys())
        new_day_timers_and_fish = dict()
        for timer in current_timers:
            if timer == 0:
                new_day_timers_and_fish[8] = timers_and_fish[0]
                sixth_timers = new_day_timers_and_fish.setdefault(6,0)
                new_day_timers_and_fish[6] = timers_and_fish[0] + sixth_timers
            else:
                fishes_with_timer = new_day_timers_and_fish.setdefault(timer-1,0)
                new_day_timers_and_fish[timer-1] = timers_and_fish[timer] + fishes_with_timer

        timers_and_fish = new_day_timers_and_fish
    
    print(sum(timers_and_fish.values()))
    

            



if __name__ == '__main__':
    main()
