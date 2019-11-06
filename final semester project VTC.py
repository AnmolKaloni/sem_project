
# coding: utf-8

# In[2]:


from tkinter import *   
  
  
top = Tk()  

  
top.geometry("400x400")

l=Label(top,text="Anmol Assistant!")
l.pack()


def buttonClick():
    import speech_recognition as sr
    top.geometry("400x400")
    l=Label(top,text="Say Anything")
    l.pack()

    r=sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)

        audio= r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            top.geometry("400x400")
            l=Label(top,text=text)
            l.pack()
        except:
            print("sorry, could not recognise")
  
b = Button(top,text = "Click me",command=buttonClick) 
  
b.pack()  
  
top.mainloop()


   
       
       


    

