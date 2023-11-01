
import statistics
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.size = 30
        self.map = [None] * self.size
        self.count = [0] * (self.size)

    def _get_hash(self, key):
        hash_value = hash(key) % self.size
        self.count[hash_value] += 1
        return hash_value

    def put(self, key, value):
        hash_value = self._get_hash(key)

        if self.map[hash_value] is None:
            self.map[hash_value] = Node(key, value)
        else:
            node = self.map[hash_value]
            while True:
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    break
                node = node.next

            node.next = Node(key, value)

    def count_words(self, text):
        words = text.split()

        for word in words:
            word = word.lower()
            word = word.strip(".,?!")

            if word:
                if self.get(word):
                    self.put(word, self.get(word) + 1)
                else:
                    self.put(word, 1)

    def get(self, key):
        hash_value = self._get_hash(key)

        node = self.map[hash_value]
        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def print_keys(self):
        keys = []
        for node in self.map:
            while node:
                keys.append(node.key)
                print(node.key)
                node = node.next

    def print_values(self):
        values = []
        for node in self.map:
            while node:
                values.append([node.key, node.value])
                node = node.next
        for Pair in values:
            print(self._get_hash(node.key), Pair)

    def get_count(self):
        print(self.count)
        hist, bin_edges = statistics.histogram(data, bins=5)


map = HashMap()
text="""The Project Gutenberg EBook of Alice in Wonderland, by Lewis Carroll

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: Alice in Wonderland

Author: Lewis Carroll

Illustrator: Gordon Robinson

Release Date: August 12, 2006 [EBook #19033]

Language: English

Character set encoding: ISO-8859-1

*** START OF THIS PROJECT GUTENBERG EBOOK ALICE IN WONDERLAND ***




Produced by Jason Isbell, Irma Spehar, and the Online
Distributed Proofreading Team at http://www.pgdp.net









          [Illustration: Alice in the Room of the Duchess.]


                       _THE "STORYLAND" SERIES_



                   ALICE'S ADVENTURES IN WONDERLAND







                     SAM'L GABRIEL SONS & COMPANY

                               NEW YORK



                           Copyright, 1916,

                   by SAM'L GABRIEL SONS & COMPANY

                               NEW YORK




ALICE'S ADVENTURES IN WONDERLAND

[Illustration]




I--DOWN THE RABBIT-HOLE


Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do. Once or twice she had peeped into the
book her sister was reading, but it had no pictures or conversations in
it, "and what is the use of a book," thought Alice, "without pictures or
conversations?"

So she was considering in her own mind (as well as she could, for the
day made her feel very sleepy and stupid), whether the pleasure of
making a daisy-chain would be worth the trouble of getting up and
picking the daisies, when suddenly a White Rabbit with pink eyes ran
close by her.

There was nothing so very remarkable in that, nor did Alice think it so
very much out of the way to hear the Rabbit say to itself, "Oh dear! Oh
dear! I shall be too late!" But when the Rabbit actually took a watch
out of its waistcoat-pocket and looked at it and then hurried on, Alice
started to her feet, for it flashed across her mind that she had never
before seen a rabbit with either a waistcoat-pocket, or a watch to take
out of it, and, burning with curiosity, she ran across the field after
it and was just in time to see it pop down a large rabbit-hole, under
the hedge. In another moment, down went Alice after it!

[Illustration]

The rabbit-hole went straight on like a tunnel for some way and then
dipped suddenly down, so suddenly that Alice had not a moment to think
about stopping herself before she found herself falling down what seemed
to be a very deep well.

Either the well was very deep, or she fell very slowly, for she had
plenty of time, as she went down, to look about her. First, she tried to
make out what she was coming to, but it was too dark to see anything;
then she looked at the sides of the well and noticed that they were
filled with cupboards and book-shelves; here and there she saw maps and
pictures hung upon pegs. She took down a jar from one of the shelves as
she passed. It was labeled "ORANGE MARMALADE," but, to her great
disappointment, it was empty; she did not like to drop the jar, so
managed to put it into one of the cupboards as she fell past it.

Down, down, down! Would the fall never come to an end? There was nothing
else to do, so Alice soon began talking to herself. "Dinah'll miss me
very much to-night, I should think!" (Dinah was the cat.) "I hope
they'll remember her saucer of milk at tea-time. Dinah, my dear, I wish
you were down here with me!" Alice felt that she was dozing off, when
suddenly, thump! thump! down she came upon a heap of sticks and dry
leaves, and the fall was over.

Alice was not a bit hurt, and she jumped up in a moment. She looked up,
but it was all dark overhead; before her was another long passage and
the White Rabbit was still in sight, hurrying down it. There was not a
moment to be lost. Away went Alice like the wind and was just in time to
hear it say, as it turned a corner, "Oh, my ears and whiskers, how late
it's getting!" She was close behind it when she turned the corner, but
the Rabbit was no longer to be seen.

She found herself in a long, low hall, which was lit up by a row of
lamps hanging from the roof. There were doors all 'round the hall, but
they were all locked; and when Alice had been all the way down one side
and up the other, trying every door, she walked sadly down the middle,
wondering how she was ever to get out again.

Suddenly she came upon a little table, all made of solid glass. There
was nothing on it but a tiny golden key, and Alice's first idea was that
this might belong to one of the doors of the hall; but, alas! either the
locks were too large, or the key was too small, but, at any rate, it
would not open any of them. However, on the second time 'round, she came
upon a low curtain she had not noticed before, and behind it was a
little door about fifteen inches high. She tried the little golden key
in the lock, and to her great delight, it fitted!

[Illustration]

Alice opened the door and found that it led into a small passage, not
much larger than a rat-hole; she knelt down and looked along the passage
into the loveliest garden you ever saw. How she longed to get out of
that dark hall and wander about among those beds of bright flowers and
those cool fountains, but she could not even get her head through the
doorway. "Oh," said Alice, "how I wish I could shut up like a telescope!
I think I could, if I only knew how to begin."

Alice went back to the table, half hoping she might find another key on
it, or at any rate, a book of rules for shutting people up like
telescopes. This time she found a little bottle on it ("which certainly
was not here before," said Alice), and tied 'round the neck of the
bottle was a paper label, with the words "DRINK ME" beautifully printed
on it in large letters.

"No, I'll look first," she said, "and see whether it's marked '_poison_'
or not," for she had never forgotten that, if you drink from a bottle
marked "poison," it is almost certain to disagree with you, sooner or
later. However, this bottle was _not_ marked "poison," so Alice ventured
to taste it, and, finding it very nice (it had a sort of mixed flavor of
cherry-tart, custard, pineapple, roast turkey, toffy and hot buttered
toast), she very soon finished it off.

       *       *       *       *       *

"What a curious feeling!" said Alice. "I must be shutting up like a
telescope!"

And so it was indeed! She was now only ten inches high, and her face
brightened up at the thought that she was now the right size for going
through the little door into that lovely garden.

After awhile, finding that nothing more happened, she decided on going
into the garden at once; but, alas for poor Alice! When she got to the
door, she found she had forgotten the little golden key, and when she
went back to the table for it, she found she could not possibly reach
it: she could see it quite plainly through the glass and she tried her
best to climb up one of the legs of the table, but it was too slippery,
and when she had tired herself out with trying, the poor little thing
sat down and cried.

"Come, there's no use in crying like that!" said Alice to herself rather
sharply. "I advise you to leave off this minute!" She generally gave
herself very good advice (though she very seldom followed it), and
sometimes she scolded herself so severely as to bring tears into her
eyes.

Soon her eye fell on a little glass box that was lying under the table:
she opened it and found in it a very small cake, on which the words "EAT
ME" were beautifully marked in currants. "Well, I'll eat it," said
Alice, "and if it makes me grow larger, I can reach the key; and if it
makes me grow smaller, I can creep under the door: so either way I'll
get into the garden, and I don't care which happens!"

She ate a little bit and said anxiously to herself, "Which way? Which
way?" holding her hand on the top of her head to feel which way she was
growing; and she was quite surprised to find that she remained the same
size. So she set to work and very soon finished off the cake.

[Illustration]




II--THE POOL OF TEARS


"Curiouser and curiouser!" cried Alice (she was so much surprised that
for the moment she quite forgot how to speak good English). "Now I'm
opening out like the largest telescope that ever was! Good-by, feet! Oh,
my poor little feet, I wonder who will put on your shoes and stockings
for you now, dears? I shall be a great deal too far off to trouble
myself about you."

Just at this moment her head struck against the roof of the hall; in
fact, she was now rather more than nine feet high, and she at once took
up the little golden key and hurried off to the garden door.

Poor Alice! It was as much as she could do, lying down on one side, to
look through into the garden with one eye; but to get through was more
hopeless than ever. She sat down and began to cry again.

She went on shedding gallons of tears, until there was a large pool all
'round her and reaching half down the hall.

After a time, she heard a little pattering of feet in the distance and
she hastily dried her eyes to see what was coming. It was the White
Rabbit returning, splendidly dressed, with a pair of white kid-gloves in
one hand and a large fan in the other. He came trotting along in a
great hurry, muttering to himself, "Oh! the Duchess, the Duchess! Oh!
_won't_ she be savage if I've kept her waiting!"

When the Rabbit came near her, Alice began, in a low, timid voice, "If
you please, sir--" The Rabbit started violently, dropped the white
kid-gloves and the fan and skurried away into the darkness as hard as he
could go.

[Illustration]

Alice took up the fan and gloves and she kept fanning herself all the
time she went on talking. "Dear, dear! How queer everything is to-day!
And yesterday things went on just as usual. _Was_ I the same when I got
up this morning? But if I'm not the same, the next question is, 'Who in
the world am I?' Ah, _that's_ the great puzzle!"

As she said this, she looked down at her hands and was surprised to see
that she had put on one of the Rabbit's little white kid-gloves while
she was talking. "How _can_ I have done that?" she thought. "I must be
growing small again." She got up and went to the table to measure
herself by it and found that she was now about two feet high and was
going on shrinking rapidly. She soon found out that the cause of this
was the fan she was holding and she dropped it hastily, just in time to
save herself from shrinking away altogether.

"That _was_ a narrow escape!" said Alice, a good deal frightened at the
sudden change, but very glad to find herself still in existence. "And
now for the garden!" And she ran with all speed back to the little door;
but, alas! the little door was shut again and the little golden key was
lying on the glass table as before. "Things are worse than ever,"
thought the poor child, "for I never was so small as this before,
never!"

As she said these words, her foot slipped, and in another moment,
splash! she was up to her chin in salt-water. Her first idea was that
she had somehow fallen into the sea. However, she soon made out that she
was in the pool of tears which she had wept when she was nine feet high.

[Illustration]

Just then she heard something splashing about in the pool a little way
off, and she swam nearer to see what it was: she soon made out that it
was only a mouse that had slipped in like herself.

"Would it be of any use, now," thought Alice, "to speak to this mouse?
Everything is so out-of-the-way down here that I should think very
likely it can talk; at any rate, there's no harm in trying." So she
began, "O Mouse, do you know the way out of this pool? I am very tired
of swimming about here, O Mouse!" The Mouse looked at her rather
inquisitively and seemed to her to wink with one of its little eyes, but
it said nothing.

"Perhaps it doesn't understand English," thought Alice. "I dare say it's
a French mouse, come over with William the Conqueror." So she began
again: "O� est ma chatte?" which was the first sentence in her French
lesson-book. The Mouse gave a sudden leap out of the water and seemed to
quiver all over with fright. "Oh, I beg your pardon!" cried Alice
hastily, afraid that she had hurt the poor animal's feelings. "I quite
forgot you didn't like cats."

"Not like cats!" cried the Mouse in a shrill, passionate voice. "Would
_you_ like cats, if you were me?"

"Well, perhaps not," said Alice in a soothing tone; "don't be angry
about it. And yet I wish I could show you our cat Dinah. I think you'd
take a fancy to cats, if you could only see her. She is such a dear,
quiet thing." The Mouse was bristling all over and she felt certain it
must be really offended. "We won't talk about her any more, if you'd
rather not."

"We, indeed!" cried the Mouse, who was trembling down to the end of its
tail. "As if _I_ would talk on such a subject! Our family always _hated_
cats--nasty, low, vulgar things! Don't let me hear the name again!"

[Illustration: Alice at the Mad Tea Party.]

"I won't indeed!" said Alice, in a great hurry to change the subject of
conversation. "Are you--are you fond--of--of dogs? There is such a nice
little dog near our house, I should like to show you! It kills all the
rats and--oh, dear!" cried Alice in a sorrowful tone. "I'm afraid I've
offended it again!" For the Mouse was swimming away from her as hard as
it could go, and making quite a commotion in the pool as it went.

So she called softly after it, "Mouse dear! Do come back again, and we
won't talk about cats, or dogs either, if you don't like them!" When the
Mouse heard this, it turned 'round and swam slowly back to her; its face
was quite pale, and it said, in a low, trembling voice, "Let us get to
the shore and then I'll tell you my history and you'll understand why it
is I hate cats and dogs."

It was high time to go, for the pool was getting quite crowded with the
birds and animals that had fallen into it; there were a Duck and a Dodo,
a Lory and an Eaglet, and several other curious creatures. Alice led the
way and the whole party swam to the shore.

[Illustration]




III--A CAUCUS-RACE AND A LONG TALE


They were indeed a queer-looking party that assembled on the bank--the
birds with draggled feathers, the animals with their fur clinging close
to them, and all dripping wet, cross and uncomfortable.

[Illustration]

The first question, of course, was how to get dry again. They had a
consultation about this and after a few minutes, it seemed quite natural
to Alice to find herself talking familiarly with them, as if she had
known them all her life.

At last the Mouse, who seemed to be a person of some authority among
them, called out, "Sit down, all of you, and listen to me! _I'll_ soon
make you dry enough!" They all sat down at once, in a large ring, with
the Mouse in the middle.

"Ahem!" said the Mouse with an important air. "Are you all ready? This
is the driest thing I know. Silence all 'round, if you please! 'William
the Conqueror, whose cause was favored by the pope, was soon submitted
to by the English, who wanted leaders, and had been of late much
accustomed to usurpation and conquest. Edwin and Morcar, the Earls of
Mercia and Northumbria'--"

"Ugh!" said the Lory, with a shiver.

"--'And even Stigand, the patriotic archbishop of Canterbury, found it
advisable'--"

"Found _what_?" said the Duck.

"Found _it_," the Mouse replied rather crossly; "of course, you know
what 'it' means."

"I know what 'it' means well enough, when _I_ find a thing," said the
Duck; "it's generally a frog or a worm. The question is, what did the
archbishop find?"

The Mouse did not notice this question, but hurriedly went on, "'--found
it advisable to go with Edgar Atheling to meet William and offer him the
crown.'--How are you getting on now, my dear?" it continued, turning to
Alice as it spoke.

"As wet as ever," said Alice in a melancholy tone; "it doesn't seem to
dry me at all."

"In that case," said the Dodo solemnly, rising to its feet, "I move that
the meeting adjourn, for the immediate adoption of more energetic
remedies--"

"Speak English!" said the Eaglet. "I don't know the meaning of half
those long words, and, what's more, I don't believe you do either!"

"What I was going to say," said the Dodo in an offended tone, "is that
the best thing to get us dry would be a Caucus-race."

"What _is_ a Caucus-race?" said Alice.

[Illustration]

"Why," said the Dodo, "the best way to explain it is to do it." First it
marked out a race-course, in a sort of circle, and then all the party
were placed along the course, here and there. There was no "One, two,
three and away!" but they began running when they liked and left off
when they liked, so that it was not easy to know when the race was over.
However, when they had been running half an hour or so and were quite
dry again, the Dodo suddenly called out, "The race is over!" and they
all crowded 'round it, panting and asking, "But who has won?"

This question the Dodo could not answer without a great deal of thought.
At last it said, "_Everybody_ has won, and _all_ must have prizes."

"But who is to give the prizes?" quite a chorus of voices asked.

"Why, _she_, of course," said the Dodo, pointing to Alice with one
finger; and the whole party at once crowded 'round her, calling out, in
a confused way, "Prizes! Prizes!"

Alice had no idea what to do, and in despair she put her hand into her
pocket and pulled out a box of comfits (luckily the salt-water had not
got into it) and handed them 'round as prizes. There was exactly one
a-piece, all 'round.

The next thing was to eat the comfits; this caused some noise and
confusion, as the large birds complained that they could not taste
theirs, and the small ones choked and had to be patted on the back.
However, it was over at last and they sat down again in a ring and
begged the Mouse to tell them something more.

"You promised to tell me your history, you know," said Alice, "and why
it is you hate--C and D," she added in a whisper, half afraid that it
would be offended again.

"Mine is a long and a sad tale!" said the Mouse, turning to Alice and
sighing.

"It _is_ a long tail, certainly," said Alice, looking down with wonder
at the Mouse's tail, "but why do you call it sad?" And she kept on
puzzling about it while the Mouse was speaking, so that her idea of the
tale was something like this:--

    "Fury said to
      a mouse, That
         he met in the
            house, 'Let
              us both go
                to law: _I_
                 will prosecute
               _you_.--
                 Come, I'll
              take no denial:
             We
           must have
        the trial;
     For really
    this morning
    I've
    nothing
    to do.'
    Said the
     mouse to
      the cur,
       'Such a
        trial, dear
           sir, With
               no jury
                or judge,
                   would
                  be wasting
                our
             breath.'
         'I'll be
        judge,
       I'll be
      jury,'
     said
    cunning
    old
     Fury;
      'I'll
       try
        the
         whole
          cause,
          and
         condemn
       you to
    death.'"

"You are not attending!" said the Mouse to Alice, severely. "What are
you thinking of?"

"I beg your pardon," said Alice very humbly, "you had got to the fifth
bend, I think?"

"You insult me by talking such nonsense!" said the Mouse, getting up and
walking away.

"Please come back and finish your story!" Alice called after it. And the
others all joined in chorus, "Yes, please do!" But the Mouse only shook
its head impatiently and walked a little quicker.

"I wish I had Dinah, our cat, here!" said Alice. This caused a
remarkable sensation among the party. Some of the birds hurried off at
once, and a Canary called out in a trembling voice, to its children,
"Come away, my dears! It's high time you were all in bed!" On various
pretexts they all moved off and Alice was soon left alone.

"I wish I hadn't mentioned Dinah! Nobody seems to like her down here and
I'm sure she's the best cat in the world!" Poor Alice began to cry
again, for she felt very lonely and low-spirited. In a little while,
however, she again heard a little pattering of footsteps in the distance
and she looked up eagerly.

[Illustration]

[Illustration]




IV--THE RABBIT SENDS IN A LITTLE BILL


It was the White Rabbit, trotting slowly back again and looking
anxiously about as it went, as if it had lost something; Alice heard it
muttering to itself, "The Duchess! The Duchess! Oh, my dear paws! Oh, my
fur and whiskers! She'll get me executed, as sure as ferrets are
ferrets! Where _can_ I have dropped them, I wonder?" Alice guessed in a
moment that it was looking for the fan and the pair of white kid-gloves
and she very good-naturedly began hunting about for them, but they were
nowhere to be seen--everything seemed to have changed since her swim in
the pool, and the great hall, with the glass table and the little door,
had vanished completely.

Very soon the Rabbit noticed Alice, and called to her, in an angry tone,
"Why, Mary Ann, what _are_ you doing out here? Run home this moment and
fetch me a pair of gloves and a fan! Quick, now!"

"He took me for his housemaid!" said Alice, as she ran off. "How
surprised he'll be when he finds out who I am!" As she said this, she
came upon a neat little house, on the door of which was a bright brass
plate with the name "W. RABBIT" engraved upon it. She went in without
knocking and hurried upstairs, in great fear lest she should meet the
real Mary Ann and be turned out of the house before she had found the
fan and gloves.

By this time, Alice had found her way into a tidy little room with a
table in the window, and on it a fan and two or three pairs of tiny
white kid-gloves; she took up the fan and a pair of the gloves and was
just going to leave the room, when her eyes fell upon a little bottle
that stood near the looking-glass. She uncorked it and put it to her
lips, saying to herself, "I do hope it'll make me grow large again, for,
really, I'm quite tired of being such a tiny little thing!"

Before she had drunk half the bottle, she found her head pressing
against the ceiling, and had to stoop to save her neck from being
broken. She hastily put down the bottle, remarking, "That's quite
enough--I hope I sha'n't grow any more."

Alas! It was too late to wish that! She went on growing and growing and
very soon she had to kneel down on the floor. Still she went on growing,
and, as a last resource, she put one arm out of the window and one foot
up the chimney, and said to herself, "Now I can do no more, whatever
happens. What _will_ become of me?"

[Illustration]

Luckily for Alice, the little magic bottle had now had its full effect
and she grew no larger. After a few minutes she heard a voice outside
and stopped to listen.

"Mary Ann! Mary Ann!" said the voice. "Fetch me my gloves this moment!"
Then came a little pattering of feet on the stairs. Alice knew it was
the Rabbit coming to look for her and she trembled till she shook the
house, quite forgetting that she was now about a thousand times as large
as the Rabbit and had no reason to be afraid of it.

Presently the Rabbit came up to the door and tried to open it; but as
the door opened inwards and Alice's elbow was pressed hard against it,
that attempt proved a failure. Alice heard it say to itself, "Then I'll
go 'round and get in at the window."

"_That_ you won't!" thought Alice; and after waiting till she fancied
she heard the Rabbit just under the window, she suddenly spread out her
hand and made a snatch in the air. She did not get hold of anything,
but she heard a little shriek and a fall and a crash of broken glass,
from which she concluded that it was just possible it had fallen into a
cucumber-frame or something of that sort.

Next came an angry voice--the Rabbit's--"Pat! Pat! Where are you?" And
then a voice she had never heard before, "Sure then, I'm here! Digging
for apples, yer honor!"

"Here! Come and help me out of this! Now tell me, Pat, what's that in
the window?"

"Sure, it's an arm, yer honor!"

"Well, it's got no business there, at any rate; go and take it away!"

There was a long silence after this and Alice could only hear whispers
now and then, and at last she spread out her hand again and made another
snatch in the air. This time there were _two_ little shrieks and more
sounds of broken glass. "I wonder what they'll do next!" thought Alice.
"As for pulling me out of the window, I only wish they _could_!"

She waited for some time without hearing anything more. At last came a
rumbling of little cart-wheels and the sound of a good many voices all
talking together. She made out the words: "Where's the other ladder?
Bill's got the other--Bill! Here, Bill! Will the roof bear?--Who's to go
down the chimney?--Nay, _I_ sha'n't! _You_ do it! Here, Bill! The master
says you've got to go down the chimney!"

Alice drew her foot as far down the chimney as she could and waited till
she heard a little animal scratching and scrambling about in the chimney
close above her; then she gave one sharp kick and waited to see what
would happen next.

The first thing she heard was a general chorus of "There goes Bill!"
then the Rabbit's voice alone--"Catch him, you by the hedge!" Then
silence and then another confusion of voices--"Hold up his head--Brandy
now--Don't choke him--What happened to you?"

Last came a little feeble, squeaking voice, "Well, I hardly know--No
more, thank ye. I'm better now--all I know is, something comes at me
like a Jack-in-the-box and up I goes like a sky-rocket!"

After a minute or two of silence, they began moving about again, and
Alice heard the Rabbit say, "A barrowful will do, to begin with."

"A barrowful of _what_?" thought Alice. But she had not long to doubt,
for the next moment a shower of little pebbles came rattling in at the
window and some of them hit her in the face. Alice noticed, with some
surprise, that the pebbles were all turning into little cakes as they
lay on the floor and a bright idea came into her head. "If I eat one of
these cakes," she thought, "it's sure to make _some_ change in my size."

So she swallowed one of the cakes and was delighted to find that she
began shrinking directly. As soon as she was small enough to get through
the door, she ran out of the house and found quite a crowd of little
animals and birds waiting outside. They all made a rush at Alice the
moment she appeared, but she ran off as hard as she could and soon found
herself safe in a thick wood.

[Illustration: "The Duchess tucked her arm affectionately into
Alice's."]

"The first thing I've got to do," said Alice to herself, as she
wandered about in the wood, "is to grow to my right size again; and the
second thing is to find my way into that lovely garden. I suppose I
ought to eat or drink something or other, but the great question is
'What?'"

Alice looked all around her at the flowers and the blades of grass, but
she could not see anything that looked like the right thing to eat or
drink under the circumstances. There was a large mushroom growing near
her, about the same height as herself. She stretched herself up on
tiptoe and peeped over the edge and her eyes immediately met those of a
large blue caterpillar, that was sitting on the top, with its arms
folded, quietly smoking a long hookah and taking not the smallest notice
of her or of anything else.

[Illustration]




V--ADVICE FROM A CATERPILLAR


At last the Caterpillar took the hookah out of its mouth and addressed
Alice in a languid, sleepy voice.

"Who are _you_?" said the Caterpillar.

[Illustration]

Alice replied, rather shyly, "I--I hardly know, sir, just at present--at
least I know who I _was_ when I got up this morning, but I think I must
have changed several times since then."

"What do you mean by that?" said the Caterpillar, sternly. "Explain
yourself!"

"I can't explain _myself_, I'm afraid, sir," said Alice, "because I'm
not myself, you see--being so many different sizes in a day is very
confusing." She drew herself up and said very gravely, "I think you
ought to tell me who _you_ are, first."

"Why?" said the Caterpillar.

As Alice could not think of any good reason and the Caterpillar seemed
to be in a _very_ unpleasant state of mind, she turned away.

"Come back!" the Caterpillar called after her. "I've something important
to say!" Alice turned and came back again.

"Keep your temper," said the Caterpillar.

"Is that all?" said Alice, swallowing down her anger as well as she
could.

"No," said the Caterpillar.

It unfolded its arms, took the hookah out of its mouth again, and said,
"So you think you're changed, do you?"

"I'm afraid, I am, sir," said Alice. "I can't remember things as I
used--and I don't keep the same size for ten minutes together!"

"What size do you want to be?" asked the Caterpillar.

"Oh, I'm not particular as to size," Alice hastily replied, "only one
doesn't like changing so often, you know. I should like to be a _little_
larger, sir, if you wouldn't mind," said Alice. "Three inches is such a
wretched height to be."

"It is a very good height indeed!" said the Caterpillar angrily, rearing
itself upright as it spoke (it was exactly three inches high).

In a minute or two, the Caterpillar got down off the mushroom and
crawled away into the grass, merely remarking, as it went, "One side
will make you grow taller, and the other side will make you grow
shorter."

"One side of _what_? The other side of _what_?" thought Alice to
herself.

"Of the mushroom," said the Caterpillar, just as if she had asked it
aloud; and in another moment, it was out of sight.

Alice remained looking thoughtfully at the mushroom for a minute, trying
to make out which were the two sides of it. At last she stretched her
arms 'round it as far as they would go, and broke off a bit of the edge
with each hand.

"And now which is which?" she said to herself, and nibbled a little of
the right-hand bit to try the effect. The next moment she felt a violent
blow underneath her chin--it had struck her foot!

She was a good deal frightened by this very sudden change, as she was
shrinking rapidly; so she set to work at once to eat some of the other
bit. Her chin was pressed so closely against her foot that there was
hardly room to open her mouth; but she did it at last and managed to
swallow a morsel of the left-hand bit....

"Come, my head's free at last!" said Alice; but all she could see, when
she looked down, was an immense length of neck, which seemed to rise
like a stalk out of a sea of green leaves that lay far below her.

"Where _have_ my shoulders got to? And oh, my poor hands, how is it I
can't see you?" She was delighted to find that her neck would bend
about easily in any direction, like a serpent. She had just succeeded in
curving it down into a graceful zigzag and was going to dive in among
the leaves, when a sharp hiss made her draw back in a hurry--a large
pigeon had flown into her face and was beating her violently with its
wings.

[Illustration]

"Serpent!" cried the Pigeon.

"I'm _not_ a serpent!" said Alice indignantly. "Let me alone!"

"I've tried the roots of trees, and I've tried banks, and I've tried
hedges," the Pigeon went on, "but those serpents! There's no pleasing
them!"

Alice was more and more puzzled.

"As if it wasn't trouble enough hatching the eggs," said the Pigeon,
"but I must be on the look-out for serpents, night and day! And just as
I'd taken the highest tree in the wood," continued the Pigeon, raising
its voice to a shriek, "and just as I was thinking I should be free of
them at last, they must needs come wriggling down from the sky! Ugh,
Serpent!"

"But I'm _not_ a serpent, I tell you!" said Alice. "I'm a--I'm a--I'm a
little girl," she added rather doubtfully, as she remembered the number
of changes she had gone through that day.

"You're looking for eggs, I know _that_ well enough," said the Pigeon;
"and what does it matter to me whether you're a little girl or a
serpent?"

"It matters a good deal to _me_," said Alice hastily; "but I'm not
looking for eggs, as it happens, and if I was, I shouldn't want
_yours_--I don't like them raw."

"Well, be off, then!" said the Pigeon in a sulky tone, as it settled
down again into its nest. Alice crouched down among the trees as well as
she could, for her neck kept getting entangled among the branches, and
every now and then she had to stop and untwist it. After awhile she
remembered that she still held the pieces of mushroom in her hands, and
she set to work very carefully, nibbling first at one and then at the
other, and growing sometimes taller and sometimes shorter, until she had
succeeded in bringing herself down to her usual height.

It was so long since she had been anything near the right size that it
felt quite strange at first. "The next thing is to get into that
beautiful garden--how _is_ that to be done, I wonder?" As she said this,
she came suddenly upon an open place, with a little house in it about
four feet high. "Whoever lives there," thought Alice, "it'll never do to
come upon them _this_ size; why, I should frighten them out of their
wits!" She did not venture to go near the house till she had brought
herself down to nine inches high.




VI--PIG AND PEPPER


For a minute or two she stood looking at the house, when suddenly a
footman in livery came running out of the wood (judging by his face
only, she would have called him a fish)--and rapped loudly at the door
with his knuckles. It was opened by another footman in livery, with a
round face and large eyes like a frog.

[Illustration]

The Fish-Footman began by producing from under his arm a great letter,
and this he handed over to the other, saying, in a solemn tone, "For the
Duchess. An invitation from the Queen to play croquet." The
Frog-Footman repeated, in the same solemn tone, "From the Queen. An
invitation for the Duchess to play croquet." Then they both bowed low
and their curls got entangled together.

When Alice next peeped out, the Fish-Footman was gone, and the other was
sitting on the ground near the door, staring stupidly up into the sky.
Alice went timidly up to the door and knocked.

"There's no sort of use in knocking," said the Footman, "and that for
two reasons. First, because I'm on the same side of the door as you are;
secondly, because they're making such a noise inside, no one could
possibly hear you." And certainly there _was_ a most extraordinary noise
going on within--a constant howling and sneezing, and every now and then
a great crash, as if a dish or kettle had been broken to pieces.

"How am I to get in?" asked Alice.

"_Are_ you to get in at all?" said the Footman. "That's the first
question, you know."

Alice opened the door and went in. The door led right into a large
kitchen, which was full of smoke from one end to the other; the Duchess
was sitting on a three-legged stool in the middle, nursing a baby; the
cook was leaning over the fire, stirring a large caldron which seemed to
be full of soup.

"There's certainly too much pepper in that soup!" Alice said to herself,
as well as she could for sneezing. Even the Duchess sneezed
occasionally; and as for the baby, it was sneezing and howling
alternately without a moment's pause. The only two creatures in the
kitchen that did _not_ sneeze were the cook and a large cat, which was
grinning from ear to ear.

"Please would you tell me," said Alice, a little timidly, "why your cat
grins like that?"

"It's a Cheshire-Cat," said the Duchess, "and that's why."

"I didn't know that Cheshire-Cats always grinned; in fact, I didn't know
that cats _could_ grin," said Alice.

"You don't know much," said the Duchess, "and that's a fact."

Just then the cook took the caldron of soup off the fire, and at once
set to work throwing everything within her reach at the Duchess and the
baby--the fire-irons came first; then followed a shower of saucepans,
plates and dishes. The Duchess took no notice of them, even when they
hit her, and the baby was howling so much already that it was quite
impossible to say whether the blows hurt it or not.

"Oh, _please_ mind what you're doing!" cried Alice, jumping up and down
in an agony of terror.

"Here! You may nurse it a bit, if you like!" the Duchess said to Alice,
flinging the baby at her as she spoke. "I must go and get ready to play
croquet with the Queen," and she hurried out of the room.

Alice caught the baby with some difficulty, as it was a queer-shaped
little creature and held out its arms and legs in all directions. "If I
don't take this child away with me," thought Alice, "they're sure to
kill it in a day or two. Wouldn't it be murder to leave it behind?" She
said the last words out loud and the little thing grunted in reply.

"If you're going to turn into a pig, my dear," said Alice, "I'll have
nothing more to do with you. Mind now!"

Alice was just beginning to think to herself, "Now, what am I to do with
this creature, when I get it home?" when it grunted again so violently
that Alice looked down into its face in some alarm. This time there
could be _no_ mistake about it--it was neither more nor less than a pig;
so she set the little creature down and felt quite relieved to see it
trot away quietly into the wood.

Alice was a little startled by seeing the Cheshire-Cat sitting on a
bough of a tree a few yards off. The Cat only grinned when it saw her.
"Cheshire-Puss," began Alice, rather timidly, "would you please tell me
which way I ought to go from here?"

"In _that_ direction," the Cat said, waving the right paw 'round, "lives
a Hatter; and in _that_ direction," waving the other paw, "lives a March
Hare. Visit either you like; they're both mad."

"But I don't want to go among mad people," Alice remarked.

"Oh, you can't help that," said the Cat; "we're all mad here. Do you
play croquet with the Queen to-day?"

"I should like it very much," said Alice, "but I haven't been invited
yet."

"You'll see me there," said the Cat, and vanished.

Alice had not gone much farther before she came in sight of the house of
the March Hare; it was so large a house that she did not like to go near
till she had nibbled some more of the left-hand bit of mushroom.




VII--A MAD TEA-PARTY


There was a table set out under a tree in front of the house, and the
March Hare and the Hatter were having tea at it; a Dormouse was sitting
between them, fast asleep.

The table was a large one, but the three were all crowded together at
one corner of it. "No room! No room!" they cried out when they saw Alice
coming. "There's _plenty_ of room!" said Alice indignantly, and she sat
down in a large arm-chair at one end of the table.

The Hatter opened his eyes very wide on hearing this, but all he said
was "Why is a raven like a writing-desk?"

"I'm glad they've begun asking riddles--I believe I can guess that," she
added aloud.

"Do you mean that you think you can find out the answer to it?" said the
March Hare.

"Exactly so," said Alice.

"Then you should say what you mean," the March Hare went on.

"I do," Alice hastily replied; "at least--at least I mean what I
say--that's the same thing, you know."

"You might just as well say," added the Dormouse, which seemed to be
talking in its sleep, "that 'I breathe when I sleep' is the same thing
as 'I sleep when I breathe!'"

"It _is_ the same thing with you," said the Hatter, and he poured a
little hot tea upon its nose. The Dormouse shook its head impatiently
and said, without opening its eyes, "Of course, of course; just what I
was going to remark myself."

[Illustration]

"Have you guessed the riddle yet?" the Hatter said, turning to Alice
again.

"No, I give it up," Alice replied. "What's the answer?"

"I haven't the slightest idea," said the Hatter.

"Nor I," said the March Hare.

Alice gave a weary sigh. "I think you might do something better with the
time," she said, "than wasting it in asking riddles that have no
answers."

"Take some more tea," the March Hare said to Alice, very earnestly.

"I've had nothing yet," Alice replied in an offended tone, "so I can't
take more."

"You mean you can't take _less_," said the Hatter; "it's very easy to
take _more_ than nothing."

At this, Alice got up and walked off. The Dormouse fell asleep instantly
and neither of the others took the least notice of her going, though she
looked back once or twice; the last time she saw them, they were
trying to put the Dormouse into the tea-pot.

[Illustration: The Trial of the Knave of Hearts.]

"At any rate, I'll never go _there_ again!" said Alice, as she picked
her way through the wood. "It's the stupidest tea-party I ever was at in
all my life!" Just as she said this, she noticed that one of the trees
had a door leading right into it. "That's very curious!" she thought. "I
think I may as well go in at once." And in she went.

Once more she found herself in the long hall and close to the little
glass table. Taking the little golden key, she unlocked the door that
led into the garden. Then she set to work nibbling at the mushroom (she
had kept a piece of it in her pocket) till she was about a foot high;
then she walked down the little passage; and _then_--she found herself
at last in the beautiful garden, among the bright flower-beds and the
cool fountains.




VIII--THE QUEEN'S CROQUET GROUND


A large rose-tree stood near the entrance of the garden; the roses
growing on it were white, but there were three gardeners at it, busily
painting them red. Suddenly their eyes chanced to fall upon Alice, as
she stood watching them. "Would you tell me, please," said Alice, a
little timidly, "why you are painting those roses?"

Five and Seven said nothing, but looked at Two. Two began, in a low
voice, "Why, the fact is, you see, Miss, this here ought to have been a
_red_ rose-tree, and we put a white one in by mistake; and, if the Queen
was to find it out, we should all have our heads cut off, you know. So
you see, Miss, we're doing our best, afore she comes, to--" At this
moment, Five, who had been anxiously looking across the garden, called
out, "The Queen! The Queen!" and the three gardeners instantly threw
themselves flat upon their faces. There was a sound of many footsteps
and Alice looked 'round, eager to see the Queen.

First came ten soldiers carrying clubs, with their hands and feet at the
corners: next the ten courtiers; these were ornamented all over with
diamonds. After these came the royal children; there were ten of them,
all ornamented with hearts. Next came the guests, mostly Kings and
Queens, and among them Alice recognized the White Rabbit. Then followed
the Knave of Hearts, carrying the King's crown on a crimson velvet
cushion; and last of all this grand procession came THE KING AND THE
QUEEN OF HEARTS.

When the procession came opposite to Alice, they all stopped and looked
at her, and the Queen said severely, "Who is this?" She said it to the
Knave of Hearts, who only bowed and smiled in reply.

"My name is Alice, so please Your Majesty," said Alice very politely;
but she added to herself, "Why, they're only a pack of cards, after
all!"

"Can you play croquet?" shouted the Queen. The question was evidently
meant for Alice.

"Yes!" said Alice loudly.

"Come on, then!" roared the Queen.

"It's--it's a very fine day!" said a timid voice to Alice. She was
walking by the White Rabbit, who was peeping anxiously into her face.

"Very," said Alice. "Where's the Duchess?"

"Hush! Hush!" said the Rabbit. "She's under sentence of execution."

"What for?" said Alice.

"She boxed the Queen's ears--" the Rabbit began.

"Get to your places!" shouted the Queen in a voice of thunder, and
people began running about in all directions, tumbling up against each
other. However, they got settled down in a minute or two, and the game
began.

Alice thought she had never seen such a curious croquet-ground in her
life; it was all ridges and furrows. The croquet balls were live
hedgehogs, and the mallets live flamingos and the soldiers had to double
themselves up and stand on their hands and feet, to make the arches.

The players all played at once, without waiting for turns, quarrelling
all the while and fighting for the hedgehogs; and in a very short time,
the Queen was in a furious passion and went stamping about and shouting,
"Off with his head!" or "Off with her head!" about once in a minute.

"They're dreadfully fond of beheading people here," thought Alice; "the
great wonder is that there's anyone left alive!"

She was looking about for some way of escape, when she noticed a curious
appearance in the air. "It's the Cheshire-Cat," she said to herself;
"now I shall have somebody to talk to."

"How are you getting on?" said the Cat.

"I don't think they play at all fairly," Alice said, in a rather
complaining tone; "and they all quarrel so dreadfully one can't hear
oneself speak--and they don't seem to have any rules in particular."

"How do you like the Queen?" said the Cat in a low voice.

"Not at all," said Alice.

[Illustration]

Alice thought she might as well go back and see how the game was going
on. So she went off in search of her hedgehog. The hedgehog was engaged
in a fight with another hedgehog, which seemed to Alice an excellent
opportunity for croqueting one of them with the other; the only
difficulty was that her flamingo was gone across to the other side of
the garden, where Alice could see it trying, in a helpless sort of way,
to fly up into a tree. She caught the flamingo and tucked it away under
her arm, that it might not escape again.

Just then Alice ran across the Duchess (who was now out of prison). She
tucked her arm affectionately into Alice's and they walked off together.
Alice was very glad to find her in such a pleasant temper. She was a
little startled, however, when she heard the voice of the Duchess close
to her ear. "You're thinking about something, my dear, and that makes
you forget to talk."

"The game's going on rather better now," Alice said, by way of keeping
up the conversation a little.

"'Tis so," said the Duchess; "and the moral of that is--'Oh, 'tis love,
'tis love that makes the world go 'round!'"

"Somebody said," Alice whispered, "that it's done by everybody minding
his own business!"

"Ah, well! It means much the same thing," said the Duchess, digging her
sharp little chin into Alice's shoulder, as she added "and the moral of
_that_ is--'Take care of the sense and the sounds will take care of
themselves.'"

To Alice's great surprise, the Duchess's arm that was linked into hers
began to tremble. Alice looked up and there stood the Queen in front of
them, with her arms folded, frowning like a thunderstorm!

"Now, I give you fair warning," shouted the Queen, stamping on the
ground as she spoke, "either you or your head must be off, and that in
about half no time. Take your choice!" The Duchess took her choice, and
was gone in a moment.

"Let's go on with the game," the Queen said to Alice; and Alice was too
much frightened to say a word, but slowly followed her back to the
croquet-ground.

All the time they were playing, the Queen never left off quarreling with
the other players and shouting, "Off with his head!" or "Off with her
head!" By the end of half an hour or so, all the players, except the
King, the Queen and Alice, were in custody of the soldiers and under
sentence of execution.

Then the Queen left off, quite out of breath, and walked away with
Alice.

Alice heard the King say in a low voice to the company generally, "You
are all pardoned."

Suddenly the cry "The Trial's beginning!" was heard in the distance, and
Alice ran along with the others.




IX--WHO STOLE THE TARTS?


The King and Queen of Hearts were seated on their throne when they
arrived, with a great crowd assembled about them--all sorts of little
birds and beasts, as well as the whole pack of cards: the Knave was
standing before them, in chains, with a soldier on each side to guard
him; and near the King was the White Rabbit, with a trumpet in one hand
and a scroll of parchment in the other. In the very middle of the court
was a table, with a large dish of tarts upon it. "I wish they'd get the
trial done," Alice thought, "and hand 'round the refreshments!"

The judge, by the way, was the King and he wore his crown over his great
wig. "That's the jury-box," thought Alice; "and those twelve creatures
(some were animals and some were birds) I suppose they are the jurors."

Just then the White Rabbit cried out "Silence in the court!"

"Herald, read the accusation!" said the King.

[Illustration]

On this, the White Rabbit blew three blasts on the trumpet, then
unrolled the parchment-scroll and read as follows:

    "The Queen of Hearts, she made some tarts,
      All on a summer day;
    The Knave of Hearts, he stole those tarts
      And took them quite away!"

"Call the first witness," said the King; and the White Rabbit blew three
blasts on the trumpet and called out, "First witness!"

The first witness was the Hatter. He came in with a teacup in one hand
and a piece of bread and butter in the other.

"You ought to have finished," said the King. "When did you begin?"

The Hatter looked at the March Hare, who had followed him into the
court, arm in arm with the Dormouse. "Fourteenth of March, I _think_ it
was," he said.

"Give your evidence," said the King, "and don't be nervous, or I'll have
you executed on the spot."

This did not seem to encourage the witness at all; he kept shifting from
one foot to the other, looking uneasily at the Queen, and, in his
confusion, he bit a large piece out of his teacup instead of the bread
and butter.

Just at this moment Alice felt a very curious sensation--she was
beginning to grow larger again.

The miserable Hatter dropped his teacup and bread and butter and went
down on one knee. "I'm a poor man, Your Majesty," he began.

"You're a _very_ poor _speaker_," said the King.

"You may go," said the King, and the Hatter hurriedly left the court.

"Call the next witness!" said the King.

The next witness was the Duchess's cook. She carried the pepper-box in
her hand and the people near the door began sneezing all at once.

"Give your evidence," said the King.

"Sha'n't," said the cook.

The King looked anxiously at the White Rabbit, who said, in a low voice,
"Your Majesty must cross-examine _this_ witness."

"Well, if I must, I must," the King said. "What are tarts made of?"

"Pepper, mostly," said the cook.

For some minutes the whole court was in confusion and by the time they
had settled down again, the cook had disappeared.

"Never mind!" said the King, "call the next witness."

Alice watched the White Rabbit as he fumbled over the list. Imagine her
surprise when he read out, at the top of his shrill little voice, the
name "Alice!"




X--ALICE'S EVIDENCE


"Here!" cried Alice. She jumped up in such a hurry that she tipped over
the jury-box, upsetting all the jurymen on to the heads of the crowd
below.

"Oh, I _beg_ your pardon!" she exclaimed in a tone of great dismay.

"The trial cannot proceed," said the King, "until all the jurymen are
back in their proper places--_all_," he repeated with great emphasis,
looking hard at Alice.

"What do you know about this business?" the King said to Alice.

"Nothing whatever," said Alice.

The King then read from his book: "Rule forty-two. _All persons more
than a mile high to leave the court_."

"_I'm_ not a mile high," said Alice.

"Nearly two miles high," said the Queen.

[Illustration]

"Well, I sha'n't go, at any rate," said Alice.

The King turned pale and shut his note-book hastily. "Consider your
verdict," he said to the jury, in a low, trembling voice.

"There's more evidence to come yet, please Your Majesty," said the White
Rabbit, jumping up in a great hurry. "This paper has just been picked
up. It seems to be a letter written by the prisoner to--to somebody." He
unfolded the paper as he spoke and added, "It isn't a letter, after all;
it's a set of verses."

"Please, Your Majesty," said the Knave, "I didn't write it and they
can't prove that I did; there's no name signed at the end."

"You _must_ have meant some mischief, or else you'd have signed your
name like an honest man," said the King. There was a general clapping of
hands at this.

"Read them," he added, turning to the White Rabbit.

There was dead silence in the court whilst the White Rabbit read out the
verses.

"That's the most important piece of evidence we've heard yet," said the
King.

"_I_ don't believe there's an atom of meaning in it," ventured Alice.

"If there's no meaning in it," said the King, "that saves a world of
trouble, you know, as we needn't try to find any. Let the jury consider
their verdict."

"No, no!" said the Queen. "Sentence first--verdict afterwards."

"Stuff and nonsense!" said Alice loudly. "The idea of having the
sentence first!"

"Hold your tongue!" said the Queen, turning purple.

"I won't!" said Alice.

"Off with her head!" the Queen shouted at the top of her voice. Nobody
moved.

"Who cares for _you_?" said Alice (she had grown to her full size by
this time). "You're nothing but a pack of cards!"

[Illustration]

At this, the whole pack rose up in the air and came flying down upon
her; she gave a little scream, half of fright and half of anger, and
tried to beat them off, and found herself lying on the bank, with her
head in the lap of her sister, who was gently brushing away some dead
leaves that had fluttered down from the trees upon her face.

"Wake up, Alice dear!" said her sister. "Why, what a long sleep you've
had!"

"Oh, I've had such a curious dream!" said Alice. And she told her
sister, as well as she could remember them, all these strange adventures
of hers that you have just been reading about. Alice got up and ran off,
thinking while she ran, as well she might, what a wonderful dream it had
been.

[Illustration]





End of the Project Gutenberg EBook of Alice in Wonderland, by Lewis Carroll

*** END OF THIS PROJECT GUTENBERG EBOOK ALICE IN WONDERLAND ***

***** This file should be named 19033-8.txt or 19033-8.zip *****
This and all associated files of various formats will be found in:
        http://www.gutenberg.org/1/9/0/3/19033/

Produced by Jason Isbell, Irma Spehar, and the Online
Distributed Proofreading Team at http://www.pgdp.net


Updated editions will replace the previous one--the old editions
will be renamed.

Creating the works from public domain print editions means that no
one owns a United States copyright in these works, so the Foundation
(and you!) can copy and distribute it in the United States without
permission and without paying copyright royalties.  Special rules,
set forth in the General Terms of Use part of this license, apply to
copying and distributing Project Gutenberg-tm electronic works to
protect the PROJECT GUTENBERG-tm concept and trademark.  Project
Gutenberg is a registered trademark, and may not be used if you
charge for the eBooks, unless you receive specific permission.  If you
do not charge anything for copies of this eBook, complying with the
rules is very easy.  You may use this eBook for nearly any purpose
such as creation of derivative works, reports, performances and
research.  They may be modified and printed and given away--you may do
practically ANYTHING with public domain eBooks.  Redistribution is
subject to the trademark license, especially commercial
redistribution.



*** START: FULL LICENSE ***

THE FULL PROJECT GUTENBERG LICENSE
PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg-tm mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase "Project
Gutenberg"), you agree to comply with all the terms of the Full Project
Gutenberg-tm License (available with this file or online at
http://gutenberg.org/license).


Section 1.  General Terms of Use and Redistributing Project Gutenberg-tm
electronic works

1.A.  By reading or using any part of this Project Gutenberg-tm
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement.  If you do not agree to abide by all
the terms of this agreement, you must cease using and return or destroy
all copies of Project Gutenberg-tm electronic works in your possession.
If you paid a fee for obtaining a copy of or access to a Project
Gutenberg-tm electronic work and you do not agree to be bound by the
terms of this agreement, you may obtain a refund from the person or
entity to whom you paid the fee as set forth in paragraph 1.E.8.

1.B.  "Project Gutenberg" is a registered trademark.  It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement.  There are a few
things that you can do with most Project Gutenberg-tm electronic works
even without complying with the full terms of this agreement.  See
paragraph 1.C below.  There are a lot of things you can do with Project
Gutenberg-tm electronic works if you follow the terms of this agreement
and help preserve free future access to Project Gutenberg-tm electronic
works.  See paragraph 1.E below.

1.C.  The Project Gutenberg Literary Archive Foundation ("the Foundation"
or PGLAF), owns a compilation copyright in the collection of Project
Gutenberg-tm electronic works.  Nearly all the individual works in the
collection are in the public domain in the United States.  If an
individual work is in the public domain in the United States and you are
located in the United States, we do not claim a right to prevent you from
copying, distributing, performing, displaying or creating derivative
works based on the work as long as all references to Project Gutenberg
are removed.  Of course, we hope that you will support the Project
Gutenberg-tm mission of promoting free access to electronic works by
freely sharing Project Gutenberg-tm works in compliance with the terms of
this agreement for keeping the Project Gutenberg-tm name associated with
the work.  You can easily comply with the terms of this agreement by
keeping this work in the same format with its attached full Project
Gutenberg-tm License when you share it without charge with others.

1.D.  The copyright laws of the place where you are located also govern
what you can do with this work.  Copyright laws in most countries are in
a constant state of change.  If you are outside the United States, check
the laws of your country in addition to the terms of this agreement
before downloading, copying, displaying, performing, distributing or
creating derivative works based on this work or any other Project
Gutenberg-tm work.  The Foundation makes no representations concerning
the copyright status of any work in any country outside the United
States.

1.E.  Unless you have removed all references to Project Gutenberg:

1.E.1.  The following sentence, with active links to, or other immediate
access to, the full Project Gutenberg-tm License must appear prominently
whenever any copy of a Project Gutenberg-tm work (any work on which the
phrase "Project Gutenberg" appears, or with which the phrase "Project
Gutenberg" is associated) is accessed, displayed, performed, viewed,
copied or distributed:

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org

1.E.2.  If an individual Project Gutenberg-tm electronic work is derived
from the public domain (does not contain a notice indicating that it is
posted with permission of the copyright holder), the work can be copied
and distributed to anyone in the United States without paying any fees
or charges.  If you are redistributing or providing access to a work
with the phrase "Project Gutenberg" associated with or appearing on the
work, you must comply either with the requirements of paragraphs 1.E.1
through 1.E.7 or obtain permission for the use of the work and the
Project Gutenberg-tm trademark as set forth in paragraphs 1.E.8 or
1.E.9.

1.E.3.  If an individual Project Gutenberg-tm electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any additional
terms imposed by the copyright holder.  Additional terms will be linked
to the Project Gutenberg-tm License for all works posted with the
permission of the copyright holder found at the beginning of this work.

1.E.4.  Do not unlink or detach or remove the full Project Gutenberg-tm
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg-tm.

1.E.5.  Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg-tm License.

1.E.6.  You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including any
word processing or hypertext form.  However, if you provide access to or
distribute copies of a Project Gutenberg-tm work in a format other than
"Plain Vanilla ASCII" or other format used in the official version
posted on the official Project Gutenberg-tm web site (www.gutenberg.org),
you must, at no additional cost, fee or expense to the user, provide a
copy, a means of exporting a copy, or a means of obtaining a copy upon
request, of the work in its original "Plain Vanilla ASCII" or other
form.  Any alternate format must include the full Project Gutenberg-tm
License as specified in paragraph 1.E.1.

1.E.7.  Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg-tm works
unless you comply with paragraph 1.E.8 or 1.E.9.

1.E.8.  You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg-tm electronic works provided
that

- You pay a royalty fee of 20% of the gross profits you derive from
     the use of Project Gutenberg-tm works calculated using the method
     you already use to calculate your applicable taxes.  The fee is
     owed to the owner of the Project Gutenberg-tm trademark, but he
     has agreed to donate royalties under this paragraph to the
     Project Gutenberg Literary Archive Foundation.  Royalty payments
     must be paid within 60 days following each date on which you
     prepare (or are legally required to prepare) your periodic tax
     returns.  Royalty payments should be clearly marked as such and
     sent to the Project Gutenberg Literary Archive Foundation at the
     address specified in Section 4, "Information about donations to
     the Project Gutenberg Literary Archive Foundation."

- You provide a full refund of any money paid by a user who notifies
     you in writing (or by e-mail) within 30 days of receipt that s/he
     does not agree to the terms of the full Project Gutenberg-tm
     License.  You must require such a user to return or
     destroy all copies of the works possessed in a physical medium
     and discontinue all use of and all access to other copies of
     Project Gutenberg-tm works.

- You provide, in accordance with paragraph 1.F.3, a full refund of any
     money paid for a work or a replacement copy, if a defect in the
     electronic work is discovered and reported to you within 90 days
     of receipt of the work.

- You comply with all other terms of this agreement for free
     distribution of Project Gutenberg-tm works.

1.E.9.  If you wish to charge a fee or distribute a Project Gutenberg-tm
electronic work or group of works on different terms than are set
forth in this agreement, you must obtain permission in writing from
both the Project Gutenberg Literary Archive Foundation and Michael
Hart, the owner of the Project Gutenberg-tm trademark.  Contact the
Foundation as set forth in Section 3 below.

1.F.

1.F.1.  Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
public domain works in creating the Project Gutenberg-tm
collection.  Despite these efforts, Project Gutenberg-tm electronic
works, and the medium on which they may be stored, may contain
"Defects," such as, but not limited to, incomplete, inaccurate or
corrupt data, transcription errors, a copyright or other intellectual
property infringement, a defective or damaged disk or other medium, a
computer virus, or computer codes that damage or cannot be read by
your equipment.

1.F.2.  LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the "Right
of Replacement or Refund" described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg-tm trademark, and any other party distributing a Project
Gutenberg-tm electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees.  YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH F3.  YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.

1.F.3.  LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from.  If you
received the work on a physical medium, you must return the medium with
your written explanation.  The person or entity that provided you with
the defective work may elect to provide a replacement copy in lieu of a
refund.  If you received the work electronically, the person or entity
providing it to you may choose to give you a second opportunity to
receive the work electronically in lieu of a refund.  If the second copy
is also defective, you may demand a refund in writing without further
opportunities to fix the problem.

1.F.4.  Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you 'AS-IS' WITH NO OTHER
WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
WARRANTIES OF MERCHANTIBILITY OR FITNESS FOR ANY PURPOSE.

1.F.5.  Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of damages.
If any disclaimer or limitation set forth in this agreement violates the
law of the state applicable to this agreement, the agreement shall be
interpreted to make the maximum disclaimer or limitation permitted by
the applicable state law.  The invalidity or unenforceability of any
provision of this agreement shall not void the remaining provisions.

1.F.6.  INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg-tm electronic works in accordance
with this agreement, and any volunteers associated with the production,
promotion and distribution of Project Gutenberg-tm electronic works,
harmless from all liability, costs and expenses, including legal fees,
that arise directly or indirectly from any of the following which you do
or cause to occur: (a) distribution of this or any Project Gutenberg-tm
work, (b) alteration, modification, or additions or deletions to any
Project Gutenberg-tm work, and (c) any Defect you cause.


Section  2.  Information about the Mission of Project Gutenberg-tm

Project Gutenberg-tm is synonymous with the free distribution of
electronic works in formats readable by the widest variety of computers
including obsolete, old, middle-aged and new computers.  It exists
because of the efforts of hundreds of volunteers and donations from
people in all walks of life.

Volunteers and financial support to provide volunteers with the
assistance they need, is critical to reaching Project Gutenberg-tm's
goals and ensuring that the Project Gutenberg-tm collection will
remain freely available for generations to come.  In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg-tm and future generations.
To learn more about the Project Gutenberg Literary Archive Foundation
and how your efforts and donations can help, see Sections 3 and 4
and the Foundation web page at http://www.pglaf.org.


Section 3.  Information about the Project Gutenberg Literary Archive
Foundation

The Project Gutenberg Literary Archive Foundation is a non profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service.  The Foundation's EIN or federal tax identification
number is 64-6221541.  Its 501(c)(3) letter is posted at
http://pglaf.org/fundraising.  Contributions to the Project Gutenberg
Literary Archive Foundation are tax deductible to the full extent
permitted by U.S. federal laws and your state's laws.

The Foundation's principal office is located at 4557 Melan Dr. S.
Fairbanks, AK, 99712., but its volunteers and employees are scattered
throughout numerous locations.  Its business office is located at
809 North 1500 West, Salt Lake City, UT 84116, (801) 596-1887, email
business@pglaf.org.  Email contact links and up to date contact
information can be found at the Foundation's web site and official
page at http://pglaf.org

For additional contact information:
     Dr. Gregory B. Newby
     Chief Executive and Director
     gbnewby@pglaf.org


Section 4.  Information about Donations to the Project Gutenberg
Literary Archive Foundation

Project Gutenberg-tm depends upon and cannot survive without wide
spread public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine readable form accessible by the widest
array of equipment including outdated equipment.  Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.

The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States.  Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements.  We do not solicit donations in locations
where we have not received written confirmation of compliance.  To
SEND DONATIONS or determine the status of compliance for any
particular state visit http://pglaf.org

While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.

International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States.  U.S. laws alone swamp our small staff.

Please check the Project Gutenberg Web pages for current donation
methods and addresses.  Donations are accepted in a number of other
ways including checks, online payments and credit card donations.
To donate, please visit: http://pglaf.org/donate


Section 5.  General Information About Project Gutenberg-tm electronic
works.

Professor Michael S. Hart is the originator of the Project Gutenberg-tm
concept of a library of electronic works that could be freely shared
with anyone.  For thirty years, he produced and distributed Project
Gutenberg-tm eBooks with only a loose network of volunteer support.


Project Gutenberg-tm eBooks are often created from several printed
editions, all of which are confirmed as Public Domain in the U.S.
unless a copyright notice is included.  Thus, we do not necessarily
keep eBooks in compliance with any particular paper edition.


Most people start at our Web site which has the main PG search facility:

     http://www.gutenberg.org

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
"""
    

map.count_words(text)
map.get_count()
