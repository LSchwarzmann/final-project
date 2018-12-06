###

Hi, welcome to VoxAnalytics!

This is the operating manual for our website and application that we have created as a final project for CS50!

To get started, visit [INSERT URL], which will lead you to our homepage. Once there, you will see multiple sections within the
website. At the top, we have a header with our logo on the left, which you can click whenever you would like to return home.
To the right, you see two options: "Convert Speech" and "Convert File"; we will continue to explain the rest of the home page
before diving into those two options of our tool.

Below the header, we included a subsection that indicates that we have built this tool for proton.ai, which is a start-up
founded by a fellow Harvard student, since we wanted to support his mission of optimizing inventory mgmt. Basically, our tool
is a first version/attempt of allowing his sales personel to record phone calls with clients and get immediate feedback on the
conversation (i.e. is the client likely to make a purchase? If so, the recording should indicate positive sentiment). The main
benefit comes in when the client is uninterested and the tool detects sufficient negative sentiment to recommend the sales
person to end the call and move on to the next customer/client. At scale, this should lead to significant time and therefore
cost reduction for proton.ai, since they will be able to determine much faster whether the call is going successful, and if
not, move on without wasting time. Needless to say, this is an early attempt that should illustrate the idea of what it could
become; of course, to make this tool realistic and give it the ability to detect emotions at a very granular (i.e. make it
extremely sensitive) level, we would have to use more advanced ML/AI algorithms that we could train with a large dataset of
previous sales calls.

Below the dark blue bar where we mention proton.ai, you see the general idea of our application as described above and a quick
start button that links to the same page as the "Convert Speech" button at the top (more on that in a bit). Further down you
see the three people that have worked on this picture, and even further below you see the a short description of the two main
features of our tool: "Convert Speech" and "Convert File".

When you click on "Convert Speech" or "Quick Start", you will be redirected to "/record", which is the speech-to-tetx feature
of VoxAnalytics. To start, press the red "listen" button on the right and say a simple sentence like 'hi how are you'. Wait
for a bit and the system will display the spoken words on the screen in black font color; black font color indicates neutral
sentiment of a word, phrase, or sentence. Next, try 'I like this song '