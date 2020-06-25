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
4. Poll server until a good appointment is found:
```bash
python fastcup.py --notify --servicecode P3039 --priority D --hospitalcode 30063 --ssn <AAABBB12X34Y567Z>
```

If there are any, FastCup will try to notify you.

#### Efficiency and ethical issues
FastCup has no ethical issues as it enhances speed and efficiency for all users and service providers (hospitals). Italian patients often tend to preemptively overbook the sanitary system. Fastcup permits to book appointments belonging to a timeframe that has probably already being cancelled by other patients. Usually appointments that are cancelled so late in time aren't scheduled at all effectively wasting the timeslot, worsening both patients and hospitals queues.
As of today there's no built-in dynamic rebooking mechanism to solve this issue.

As a result, **fastcup** only put in use timeslots that would already be wasted, enhancing hospital efficiency by using blank time, and lowering overall patients queue length by offloading long-term visits to short term, where possible.
