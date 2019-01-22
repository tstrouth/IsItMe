# IsItMe README
It is best to use photos at least 814x891, 
the required dependicies are python 3, numpy, OpenCV, and OpenCV-contrib. These are easy to install via "pip install opencv-python opencv-contrib-python"
to run this program open the command line an change directories to where the python file is saved. run "python IsItMe.py" or if running on
a GNU/Unix based platform it may be "python3 IsItMe.py" 
Press the button labeled "add 5 photos of yourself" at least 5 times and chose photos in which you wish to train the model.
Afterwards click the button labeled "add a test photo" this is the photo in which you will test against the model. It will either return a 
photo and label it "It's me" if it beleives the face in the training photos is the same face in the test photo or it will label the face 
as "it's not me" if it believes the photos do not match.

Overall, just have fun and explore concepts of Computer Vision

Continue reaidng for background on project:
When I was a senior in college for my Math Seminar we had to do a project on some field of mathematics and it's applications. During this 
time Amazon released plans for it's "cashier-less grocery stores" which used deep learning and computer vision, so that inspired me to 
do my seminar project on statistical learning and computer vision. As you may have noticed computer vision is becoming more prominent,
even can now unlock our phones and laptops using computer vision, but it also shows we have a long way to go in the field of computer vision. 
It is well known that subtle changes in faces, such as facial hair, can return a false negative or positie. I am personally very
interested in the false negatives and positives that come from the computer vision applications, which that interest sparked this project
so I can personally play with photos and see which ones return false positives or negatives.
