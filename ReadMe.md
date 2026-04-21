#Thomas Frisk
#HashSomethingOut HW 4-2
#Reflections

Have 6 because I wasn't in class for this and tried learning online. In the process I found
a hashing method I would use and improve later. Wanted to have academic honesty about it

Also had a hospital trip tonight so I rushed a bit with the merges and forgot to have the full comments there in the merge. I have the info for the commit/merges in comments if I forgot


Overall, mostly had what I expected. The bad iterations: iteration 01 and 05 were abysmal. For the linked list, it was 99% wasted space and the time on the bad linear was 19-20x worse

The second iteration of my linked list was how i learned this since I wasn't in class. I included an extra iteration because of this and i cited my source. I didn't know what the ord() function was, didn't know if it was covered in class. It was a dramatic improvement by about 33% better wasted space efficiency. The collisions were also down by orders of magnitude.

The third iteration for linked list was weird. My thought process was that whatever sum I had for the characters--even with the ord()--would bunch a lot in the same areas. So my sleep deprived idea was to then split to + and - from the midpoint. I also multiplied those values by the ord() of the first character for a better spread if it existed. Thought that would push the mean towards the center and then have a nice spread. The stats were improved but realistically that's not really what's happening in the math. Also if all the odd values are added and evens minused then I'd also get a lot of even buckets empty above and odd below. It makes sense given ~half the buckets for it were wasted for title. Quote probably got to high enough values to wrap around a bit with the modulus which is why they worked better

Fourth iteration was an improvement on the one that made the most sense and was the best. Third wasn't really one that made sense so it was a version of improvement of the one i found online. I changed it up a bit to have an addition of +3 to whatever the ith value was because when i did +0 to +5 that was the highest so that was my improvement.

fifth iteration was bad linear probing and i used the initial bad hash method for that and it was abysmal as stated before

6th iteration was by far the best. It used the best method from the linked list and had phenomenal stats overall. Just about double the time of the best linked list for title and the wasted buckets at worse down to 24% and far far better for quotes



----------------------------------------------------------------------------------
Iteration 1: the Bad, branch: movieTitle Bad

Misnomer since I was planning on multiple commits for each iteration, but I'm just passing in the same 
Information so it doesn't make sense to make one for title and one for quote.

This is a linked list hash table. 
for iteration 1, both hash table sizes are 15000 for the 15000 records in the .csv

Title as Key
Total Buckets: 15000
Wasted Buckets: 14893
Collisions: 2297776
Table time: 0.32596588134765625

Quote as Key
Total Buckets: 15000
Wasted Buckets: 14892
Collisions: 9868809
Table time: 1.1029706001281738

---------------------------------------------------------
Iteration 2: the imprvoed, branch linkedListBetter

Academic honesty, was sick as hash functions were defined in class so I looked online and
found this function at https://www.w3schools.com/python/python_dsa_hashtables.asp

I did not know things like ord() previously and I'm not counting this one towards grade,
merely academic honesty how I learned functions to try to do later hash functions

Better linked list: sum ord(char)

Title as Key
Total Buckets: 15000
Wasted Buckets: 11249
Collisions: 32188
Table time: 0.03874492645263672

Quote as Key
Total Buckets: 15000
Wasted Buckets: 10192
Collisions: 73260
Table time: 0.06971907615661621

-----------------------------------------------------------
Iteration 3: evenBetterHashFunction
for this one I wanted more variance so I started with the idea of multiplying by whatever
the value of the first character was (if it existed)

then I thought I'd vary it a bit more by multiplying by the ord() of the first character
I then thought I could vary that more by checking to see if it's even or odd. if even Information
subtract from the midpoint and if odd I add. This allowed for a better spread

iteration 03: Even Better linked list
Title as Key
Total Buckets: 15000
Wasted Buckets: 7329
Collisions: 9878
Table time: 0.0472109317779541


Quote as Key
Total Buckets: 15000
Wasted Buckets: 2726
Collisions: 18837
Table time: 0.06874704360961914

--------------------------------------------------
iteration 4: final linked hash:
So this is really an improvement on 2 because 2 was good and had room for improvement while 3 didn't really as much
because it used a kinda weird method that doesn't really work with the % in the way I was thinking.
even better for this one. Idea was to start with the index multiplied by the ord(index)
but it was bad so i kept adding one to the index and it got better till +3 then got worse at +4
so i left it at +3

time is more complex than the last but wasted buckets and collisions are down. This is best one

Title as Key
Total Buckets: 15000
Wasted Buckets: 7188
Collisions: 9169
Table time: 0.059093475341796875


Quote as Key
Total Buckets: 15000
Wasted Buckets: 2600
Collisions: 18669
Table time: 0.08672595024108887

-------------------------------
Iteration 5: bad linear

Time was abysmal for this one. So bad, but the wasted buckets was so few

iteration 05: bad linear probe
Title as Key
Total Buckets: 15000
Wasted Buckets: 3691
Collisions: 78043942
Table time: 16.025943517684937

Quote as Key
Total Buckets: 15000
Wasted Buckets: 109
Collisions: 111142876
Table time: 19.86230754852295

--------------------------------
iteration 6: good linear

I used my best linked list for this and it was the best overall for time and for wasted buckets

iteration 05: bad linear probe
Title as Key
Total Buckets: 15000
Wasted Buckets: 3691
Collisions: 126471
Table time: 0.08267903327941895

Quote as Key
Total Buckets: 15000
Wasted Buckets: 109
Collisions: 1349221
Table time: 0.3242945671081543