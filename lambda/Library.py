from Book import Book
from Page import Page
class Library:
    books = []
    currentBook = -1
    currentPage = -1
    def __init__(self):
        self.books = []
    def getTitles(self):
        returns = []
        for book in self.books:
            returns.append(book.bookName)
        return returns
    def startReadingSession(self):
        self.currentBook = self.books[0]
        self.currentPage = self.currentBook.bookStartPage
    def getText(self):
        for page in self.currentBook.pageObjs:
            if page.pageNumber == self.currentPage:
                returns = page.text
        if returns == []:
            returns = "There is no text entered for this page."
        return returns
    def getDiscussionQuestions(self):
        for page in self.currentBook.pageObjs:
            if page.pageNumber == self.currentPage:
                returns = page.discussionQuestions
        return returns
    def getShortImageDescriptions(self):
        for page in self.currentBook.pageObjs:
            if page.pageNumber == self.currentPage:
                returns = page.shortImageDescriptions
        if returns == []:
            returns = "There are no image descriptions for this page."
        return returns
    def getLongImageDescriptions(self):
        for page in self.currentBook.pageObjs:
            if page.pageNumber == self.currentPage:
                returns = page.longImageDescriptions
        if returns == ['No long description is available for this page.']:
            returns = None
        return returns
    def setPage(self, toSet):
        if (toSet <= self.currentBook.numPages) and (toSet >= self.currentBook.bookStartPage):
            self.currentPage = toSet 
            return self.currentPage
        else:
            return -1
    def nextPage(self):
        if self.currentPage == self.currentBook.numPages:
            self.currentPage = self.currentBook.bookStartPage
            return self.currentPage
        else:
            self.currentPage += 1 
            return self.currentPage
    def prevPage(self):
        if self.currentPage == self.currentBook.bookStartPage:
            return self.currentPage
        else:
            self.currentPage -= 1 
            return self.currentPage
    def createBook1(self):
        tempBook = Book("curious Geroge: A Winter's Nap", 24, 3)
        text = "One fall day, Bill and George went fishing. Bill saw George shivering. Maybe it was too cold to fish."
        shortImageDescriptions = ['On the left is Bill, a person who wears a hat, jacket, and long pants. He is sitting on the dock and looking at the character sitting on his right, George. George is a monkey who only wears a hat. He is hugging his knees close to his chest and appears to be shivering from the cold.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = ['What could Bill and George have done differently before going fishing?', 'Why do you think George felt cold?', 'Is it a good idea to fish when you feel cold?', 'How do you think Bill feels in the image?']
        page = Page(3, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "On the way home, Bill told George that some animals, such as bears, go to sleep when it gets cold. They eat a lot in the fall. "
        shortImageDescriptions = ['Pages 4 and 5 depict a single scene of Bill and George walking back home through a wooden area. Nearly bare branches and a few remaining orange leaves hint that it is fall. Bill is carrying both fishing rods and talking to George. ']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = ['what season do you think it is?']
        page = Page(4, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "Then they hibernate, or sleep, almost all winter. George was curious. If he hibernated, he would miss the cold winter months"
        shortImageDescriptions = ['Pages 4 and 5 depict a single scene of Bill and George walking back home through a wooden area. Nearly bare branches and a few remaining orange leaves hint that it is fall. Bill is carrying both fishing rods and talking to George. On the right of the pages is a close-up insert of George in a circle. He appears to be looking sideways at Bill with a curious expression.', 'On the right of the pages is a close-up insert of George in a circle. He appears to be looking sideways at Bill with a curious expression.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(5, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "At home, George ate and ate. Maybe he would get sleepy and hibernate."
        shortImageDescriptions = ['George grabbing food from the refrigerator and eating at the table at home. In the main illustration, George is smiling. He is going to put sandwiches, bananas, and other foods he grabbed from the refrigerator on a large plate, which already had grapes and other foods on it. ', 'The bottom right corner of the page is an insert of George in a circle, showing him eating a sandwich at the table with an apple on it.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = ['What types of food is George eating?']
        page = Page(6, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "Upstairs in bed, George tried to sleep. But his room was too bright"
        shortImageDescriptions = ['George lying on the bed with a red blanket and trying to sleep. The room looks well-lit. He spreads his arms and stares blankly, suggesting he has trouble falling asleep.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = ['How do you think George is feeling in this image?']
        page = Page(7, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George closed the curtains. He painted a picture of the night sky"
        shortImageDescriptions = ['George cozily lying on the bed with a white curtain closed. A painting of the night sky with stars is taped to the curtain. Next to the curtain, there is a goldfish in a bowl on a table. George is lying on the bed with his hands on his chest and eyes closed, looking peaceful, while the room is not much darker than before. In the bottom right, a circular insert shows that George is drawing a painting on an easel.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = ['Why is george putting a painting of a night sky on his curtains?']
        page = Page(8, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "He still could not sleep. How did bears do it?"
        shortImageDescriptions = ['George is lying on the bed with his eyes opened. There is a round image in upper left, depicting a bear sleeping on the bed.']
        longImageDescriptions = ['George is lying on the bed with his eyes opened. It seems like he is thinking, as his eyes are looking up. There is a round image in upper left, depicting a bear sleeping at a bed similar to George’s. The image indicates that George cannot fall asleep, as he is wondering why bears can have winter snap while he cannot. ']
        discussionQuestions = []
        page = Page(9, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        text = "George asked the man with the yellow hat about hibernation. This book says bears sleep in dark, quiet caves, said the man. That was it! George needed a cave."
        shortImageDescriptions = ['George is showing a gesture of sleeping. Behind him, a toy bear is lying on a sofa’s arm, covered by a piece of blue cloth.']
        longImageDescriptions = ['George is putting his hands together to his right cheek, showing a gesture of sleeping. Behind him, a toy bear is lying on a sofa’s arm, covered by a piece of blue cloth. The image indicates that George is trying to express his confusion about bears’ hibernation with his gesture and the toy.']
        discussionQuestions = []
        page = Page(10, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George asked the man with the yellow hat about hibernation. This book says bears sleep in dark, quiet caves, said the man. That was it! George needed a cave."
        shortImageDescriptions = ['The man in the yellow hat smiling and holding up a green book with a teddy bear on the cover. Below him, curious George reaches up towards the book, indicated by one hand in the air.\n']
        longImageDescriptions = ["The man with the yellow hat is engaging with George, who is curious but not visible in the frame except for his hands. The man, smiling gently and dressed entirely in yellow with a striped tie, holds up a small green book with a teddy bear on the cover, which discusses bear hibernation. His posture suggests he's explaining the concept to George, likely answering George's question about hibernation. The image captures the moment of learning, characteristic of George's experiences guided by the man in the yellow hat."]
        discussionQuestions = []
        page = Page(11, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George hung toy bats. He put rocks in his bed. Now his room looked like a cave."
        shortImageDescriptions = ['George is hanging a toy bat at the top of his room. He holds a green book under his arm. There is a white curtain and part of the night-sky picture behind him. ']
        longImageDescriptions = ['George hangs a toy bat from the ceiling, which is visible with the exception of the hand which is tying the string. He is holding the same green book that the man in the yellow hat gave him on the previous page. Below, although not in view, we can assume his bed is now covered with rocks to complete the cave-like atmosphere, inspired by the information about hibernation and caves that the man with the yellow hat shared with him. ']
        discussionQuestions = []
        page = Page(12, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George settled in for his long winter nap"
        shortImageDescriptions = ['George snuggling into a red blanket on a bed with a teddy bear, surrounded by a ring of grey rocks, preparing for sleep', 'George is sleeping on the bed with rocks around. He has a happy smile and is holding a toy bear.']
        longImageDescriptions = ['Page 13 depicts George lying on the bed with rocks around him. His eyes are closed. He has a happy smile and is holding a toy bear in his arm. The image shows that George has used rocks to cover his bed and made his bedroom look like a cave. Now he is trying to do a winter snap like what bears usually have.']
        discussionQuestions = ["What are the differences between George's bed and an actual cave where a bear might hibernate?", 'Which stuffed animal do you like snuggling with?']
        page = Page(13, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "Uh oh. Now what? George could hear sounds outside."
        shortImageDescriptions = ['George lying on his bed, looking alert and slightly concerned. In the inset circle, 2 pigs and 2 chickens are seen through a window, contributing to the noise that has disturbed George.', 'George is woken up, lying on his bed with the toy bear in his arm. He looks surprised and has heard something. In the bottom right, a circular insert shows two pigs and two chickens are talking and laughing.']
        longImageDescriptions = ['Page 14 depicts George being woken up, likely by some noise. He is lying on his bed, holding the toy bear. There seems to be a surprised expression on his face. The white curtain is still closed, and the painting of the night sky is taped to it. In the bottom right, a circular insert shows two pigs and two roosters are talking and laughing.']
        discussionQuestions = ['What sounds do pigs and chickens make?', 'How loud do you think they are?']
        page = Page(14, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "Pigs oinked. Cows mooed. Chickens clucked. George shushed them, but they would not be quiet."
        shortImageDescriptions = ['George outside placing a finger to his lips in a shushing gesture towards a white cow, who is leaning over a wooden fence.', 'George goes outdoors, shushing a cow inside the fence.']
        longImageDescriptions = ['Page 15 depicts George walking outdoors to the farm. He is shushing a white cow with an annoyed face, but the white cow looks unconcerned. The white cow is standing behind the fence. In the background, there is a hill and the blue sky with some white clouds. The image shows George trying to make the other animals quiet, but they are not listening to him.']
        discussionQuestions = ['Can animals understand human gestures like shushing?', 'What could be a better way for George to deal with the noise?']
        page = Page(15, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George covered his ears. The animals were not as loud. But his room was not silent yet. George taped his blanket over the window. Now it was dark and quiet."
        shortImageDescriptions = ['Pages 16 and 17 depict a single scene of George being unable to sleep and covering the window in his room with a blanket to block out noise from the animals. His room is decorated with bats, rocks, a goldfish in a glass bowl, and a red hat on the bedpost. He stands on the bed with a red blanket in hand, with which he intends to cover the window. \n', 'In the bottom left, a circular insert shows George covering his ears and his body using a red blanket. In the full image of Page 16 and 17, George is peeling off the tape with his arm and foot. Behind him, the red blanket is taped over the white curtain.']
        longImageDescriptions = ['In the bottom left, a circular insert shows George covering his ears and his body using a red blanket. He is looking to his left, indicating he finds his room is not silent. In the full image of Page 16 and 17, George is standing on the red windowsill, peeling off the tape with his arm and foot. Behind him, the red blanket is fixed on the white curtain by some pieces of tape. This image also shows a full view of George’s bedroom, in which four toy bats are hanging at the top, and some rocks are put on his bed.']
        discussionQuestions = ["What can we learn from George's attempt to silence the cow about problem-solving and dealing with situations that are out of our control?"]
        page = Page(16, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "George covered his ears. The animals were not as loud. But his room was not silent yet. George taped his blanket over the window. Now it was dark and quiet."
        shortImageDescriptions = ['Pages 16 and 17 depict a single scene of George being unable to sleep and covering the window in his room with a blanket to block out noise from the animals. His room is decorated with bats, rocks, a goldfish in a glass bowl, and a red hat on the bedpost. He stands on the bed with a red blanket in hand, with which he intends to cover the window. \r']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(17, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "Finally, George fell asleep. He slept in his monkey cave just like a bear."
        shortImageDescriptions = ['George curled up asleep in a position reminiscent of a sleeping bear in a bed surrounded by a semi-circle of rocks, mimicking a cave setting. A thought bubble above George shows a sleeping bear in a cave. ', 'George is sleeping on the bed again with rocks around. He has a happy smile and is holding a toy bear. A cloud-like insert shows a large bear sleeping in a cave and holding a little monkey.\n\n']
        longImageDescriptions = ["The culmination of George's efforts to replicate a bear's winter sleep. After attempting various strategies to make his room more conducive to hibernation, such as hanging toy bats and covering the windows to make the room dark and quiet, George finally achieves a state of rest. Surrounded by rocks he has placed to create a cave-like environment in his own bed, George mimics the slumber of a hibernating bear, symbolizing his understanding of hibernation. ", 'Page 18 depicts George sleeping on the bed again with rocks around. He has a happy smile and is holding a toy bear. A cloud-like insert shows what George thinks or dreams about: a large bear sleeping in a cave and holding George in his arms. The entrance of the cave shows the night sky and a crescent moon.']
        discussionQuestions = ['What misunderstandings does George have about hibernation?']
        page = Page(18, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "After a long time, George woke up. He had done it! He had hibernated."
        shortImageDescriptions = ['A red-roofed house amidst a pastoral landscape at dawn. In the inset circle, George is depicted waking up in his monkey cave, stretching with a satisfied expression on his face.', 'The image shows a view of George’s house and farm. The sky is purple and pink. In the bottom right, a circular insert shows George waking up on his bed with a happy smile.']
        longImageDescriptions = ["The moment after George has woken up from his attempt at hibernation. This moment highlights George's innocent triumph and his exploratory spirit, despite his misconception about the length of hibernation. ", 'Page 19 depicts a view of George’s house and farm. The sky is purple and pink, indicating it may be in the early morning. In the bottom right, a circular insert shows George waking up on his bed with a happy smile, the toy bear and some rocks are next to him.']
        discussionQuestions = ['What time of day is represented in this picture?']
        page = Page(19, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "There is no text entered for this page."
        shortImageDescriptions = ['The man in the yellow hat sitting on a stool, smiling and gesturing with one hand towards George, who is standing on the floor, holding a pillow in one hand, looking up at him with a well-rested expression.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(20, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "How did you sleep last night? asked the man; George, having slept only one night, felt sad, not realizing it wasn't all winter—then the man, struck by an idea, fetched a box of winter items."
        shortImageDescriptions = ['Likely a decorative image, the man in a yellow hat opening a closet filled with boxes.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(21, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        
        text = "The man reminded George how fun winter was. They could sled and ski together. George did not want to miss winter after all!"
        shortImageDescriptions = [' The man in a yellow hat and George dressed in a red and yellow winter suit with goggles, both preparing for winter sports. The man is holding a red sled, and George is sitting on a pair of skis, both exhibiting happy demeanors.']
        longImageDescriptions = ["This scene represents a turning point where George's perspective shifts from disappointment about not hibernating to enthusiasm for enjoying the winter with his friend."]
        discussionQuestions = ['What is sleding?', 'What is the weather like when people tend to sled?']
        page = Page(22, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        text = "When animals hibernate in winter, they sleep at a time when it might be hard for them to find food. In the fall, they start to eat lots of food to store fat. Then they rest all winter long to save energy. They wake up in the spring, ready for a new season. Bears sleep most of the winter. There are other animals that hibernate all winter long and don’t wake up at all until spring. Can you guess which animals listed include species that hibernate? bear, ladybug, cat, bat, frog, cow, pig, gopher, squirrel, skunk, monkey"
        shortImageDescriptions = ['There are no images on this page.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(23, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        
        text = "nan"
        shortImageDescriptions = ['There are no images on this page.']
        longImageDescriptions = ['No long description is available for this page.']
        discussionQuestions = []
        page = Page(24, text, shortImageDescriptions, longImageDescriptions, discussionQuestions)
        tempBook.addPage(page)
        self.books.append(tempBook)