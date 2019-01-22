# IsItMe README
It is best to use photos at least 814x891, 
the required dependicies are python 3, numpy, OpenCV, and OpenCV-contrib. These are easy to install via "pip install opencv-python opencv-contrib-python"
to run this program open the command line an change directories to where the python file is saved. run "python IsItMe.py" or if running on
a GNU/Unix based platform it may be "python3 IsItMe.py" 
Press the button labeled "add 5 photos of yourself" at least 5 times and chose photos in which you wish to train the model.
Afterwards click the button labeled "add a test photo" this is the photo in which you will test against the model. It will either return a 
photo and label it "It's me" if it beleives the face in the training photos is the same face in the test photo or it will label the face 
as "it's not me" if it believes the photos do not match.
