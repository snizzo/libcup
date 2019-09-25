# libCup + FastCUP
**libcup** is an opensource library that integrates lawful and programmatic interaction with the italian healthcare booking system, allowing for a much higher efficiency for both users and healthcare service providers.

**fastcup** is a CLI based example of a 1week hospital booker based on libcup.

### Using libCup
...

### Using FastCup
You must have one of these: red recipe / dematerialized (white) recipe.
1. Look for correct hospital service code based on your prescription:
```bash
python fastcup.py --service <query>
```
2. Look for your hospital of choice, that's offering services for your prescription with your priority (U,B,D,P):
```bash
python fastcup.py --hospital --servicecode P395 --priority P
```
3. Check availability of hospital appointments withing the timespan of 1 week:
```bash
python fastcup.py --book --servicecode P3039 --priority D --hospitalcode 30063 --ssn <AAABBB12X34Y567Z>
```

If there are any, FastCup will try to notify you.

#### Efficiency and ethical issues
FastCup has no ethical issues as it enhances speed and efficiency for all users and service providers (hospitals). Being a software that permits to book appointments withing a very short timespam it is less likely that this appointments won't be cancelled and therefore time is not wasted.

99% of the time, free timeslots are popping up because italian patients often tend to preemptively overbook the sanitary system and then cancelling appointments last minute when not needed. This leads to a major time waste for the hospitals without some timeslots free in the short term and many occupied in the long term.
As of today there's no built-in dynamic rebooking mechanism to solve this issue and **fastcup** aims exactly to that.

As a result, **fastcup** only put in use timeslots that would already be wasted, enhancing hospital efficiency by using blank time, and lowering overall patients queue length by offloading long-term visits to short term, where possible. Win-Win.
