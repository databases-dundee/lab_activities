# Lab 1 - Desigining an E-R Diagram

Good morning*! This lab is to give you practice in designing a relational database, and drawing an entity-relationship (E-R) diagram to represent this design. It's not much fun but it isn't that hard either, and it's important I promise.

<img src="erinnit.png" class="first-of-type">

## What you need to do
<img src="carpark.jpg" class="floaters">
Design an E-R diagram to model the following situation:
- A large organisation has several car parks, which are used by staff
- Each car park has a unique name, location, capacity and number of floors
- Each car park has parking spaces, which are uniquely identified by a space number
- Members of staff can request the use of a parking space; each member of staff has a unique staff number, name and phone extension number


You'll need to think about the following:
1. What are the **entities** in this scenario?
2. What **attributes** will these entities have, and what are their types?
3. Which of these attributes will make a good **Primary Key**?
4. What kinds of **relationships** will exist between the entities (e.g., one-to-many, many-to-many, one-to-one)

*This description leaves out quite a bit of detail, so you should make your own assumptions about how it should be modelled.*

## Things you can use to make the diagram

You can use whatever you like really, but here are some good things:


- [draw.io](https://app.diagrams.net/) - draw.io is a lovely tool that allows you to create diagrams and flowcharts, and export them in different file formats
- [Miro](https://www.miro.com) - Miro is an online workspace application that includes tools for diagramming and flowcharts.
- [PowerPoint](https://powerpoint.cloud.microsoft/) - I made all the lecture diagrams with it, so you could do far worse, although draw.io and Miro are probably better.
- [Pen and paper](https://www.amazon.co.uk/paper-pens/s?k=paper+and+pens) - Pen and paper is really good! Don't make it too scribbly though or I won't be able to read it.

Icing/ketchup/blood/cheddar are poor choices and should only be used in an emergency. If that sounds like a weird thing to say it's because you weren't at the lecture on Monday. To be fair it's a weird thing to say anyway.

## Anything to submit?
There's no mandatory submission here, but please do email your diagram to me at drough001@dundee.ac.uk if you want some feedback!

## Anything else?
<img src="uni.jpg" class="floaters">

If you're done with that and want some more practice (it's all helpful for your first assignment!), try the following:


Create an E-R model to encompass the following situation:
- A university requires a database to store information about its applicants, current students and graduates; this will be accessible to both staff and students
- Students are associated with a single programme of study which consists of a number of modules
- The modules may form part of multiple programmes
- The modules are taught by one (or multiple) members of staff
- Timetabling and room allocation is being done separately so does not need to be included

---
<div style="font-size:11px">
*There is actually no such thing as a good morning. All classes before noon are inherently bad and I am sorry it has to be this way.
</div>