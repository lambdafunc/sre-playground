# SRE Playground
A list of Site Reliability Engineering challenges for beginners.

# Preface
The goal of this project is to introduce you to basic SRE topics. It was designed to give an overview covered by SRE during a whole life-cycle. If you have any questions or suggestions, please do not hesitate to contact me via:
* Email [ramiz.polic@hotmail.com](mailto:ramiz.polic@hotmail.com)
* Discord [fhivemind#3230](fhivemind#3230).

## Walkthrough
We will divide this challenge into multiple stages to ease out the whole process.     

## Design
Start by thinking how the whole infrastructure can be deployed, maintained, monitored, discarded, extended, or automated. Point of this step is to have a clearer picture on how to proceed, to rule out all the improbable scenarios and major blockers. In this case, try to answer some basic questions.   

*"Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth."* - Sherlock Holmes    

---

#### :grey_question: *What is the tech-stack?*
It will give you an idea what technologies you as an SRE should continue with. Remember, you are defining the way how the whole process is going to work. Hence, you need to decide the tools you are going to be working with.     

> **Example**      
 If you are buying IKEA furniture, what tools are you going to use for its assembly?

#### :grey_question: *How does it work?*
Get a nice overview of how the solution works. Usually, here you get a lot of graphs, or you need to create them. Graphs help you get a grasp of what is happening. Some services talk to each other, some are independent, some require more memory, some require a lot of computing power. Here you need information - well-defined and concise information. Without understanding what is happening, you cannot decide what you want to happen.     

> **Example**      
Once the IKEA furniture is there, which piece connects to which? Do I need help to lift the pieces, turn them, isolate them, protect them somehow?

     
#### :grey_question: *When, and how often?*
Here, you need to think in terms of how the whole solution is going to be updated, deleted, recreated, or moved. Most likely, you will have to implement some kind of automated mechanism on how to combat these issues. Notoriously, this is the moment when **Continuous Integration (CI)**, **Continuous Deployment (CD)**, **Anything-as-a-Code (XaaS)**  comes into the picture. They are not your enemy!     

> **Example**       
Okay, you have assembled your IKEA thing, but there's a piece you forgot to add. CI allows you to define a way on how to put this piece, or any other piece you might want to add on the needed place. On the other hand, CD allows you to define a way on how to put your IKEA thing to where you want it -- in the kitchen, living room, hanging from the ceiling, or spying on your neighbors (don't do this). However, you don't want to mess up the whole darn thing, but just a pieces of it. XaaS helps you with just that, isolate a component, and do something with it -- and only that.
     
     
     
#### :grey_question: *What if?*
If you want the solution to be bullet-proof, you have to take into account on how everything is going to behave once it's up and running. These are refereed as edge-cases, and a proper solution has to cover them. Your infrastructure is built to serve US West Coast under 100ms, but what do you do for connections from India? It's Black Friday, and suddenly you have 100x higher traffic than usual. Typically, this has to do something with auto-scaling, load balancing, or networking. Your task is now to think of any case impossible scenario in which you infrastructure will fail -- and extend to support it.    

> **Example #1**      
Your IKEA furniture is a chair. However, you have 10 guests, but only 4 chairs. It's illogical to buy 10 chairs if you have 10 friends coming over only couple of times a month. So, you go and ring your neighbor, asking him to borrow you some chairs, which you will obviously return (I mean, come on, who steals chairs?). You had a nice evening, and tomorrow you return these chairs.     

> **Example #2**       
Strangely enough, one of your friends requested to NOT sit on the chair, but instead on the floor. How can he see the top of the table, eat, drink, play, and socialize?

#### :grey_question: *What is happening?*
A question you will often ask throughout the whole process. Everything is now operational, you have come this far. But, one of the services is down (perhaps, a like button on Facebook is not counting likes properly), and you don't know what to do. Here, you need to setup the Monitoring, Logging, and Observability services. They help you troubleshoot and see what is happening in realtime. They spew out a lot of unnecessary things, so correctly configuring them will help you manage everything more easily.     

> **Example**      
Remember the IKEA furniture you got? Well, you've been using it for quite some time, and you see that some of the pieces are malfunctioning. Logically, you try to determine what's the cause. Hours on end, you figure out the glue is not properly applied. And, you reapply it.

#### :grey_question: *How good is all this?*
Whenever you're building something, you need to know how well it behaves. This part is focused on answering how your infrastructure is doing, health and functional -wise. It's commonly refereed as **Service Level Agreement (SLA)** which works based on **Service Level Indicators (SLI)**. They depict legal requirements and arrangements between a buyer, and the service seller.     

> **Example**       
Before you bought your IKEA furniture, they gave you a pamphlet. On it, you read that maximum weight your furniture can hold is 200kg, it can last for 10 years on specific condition, and is designed for a specific purpose. They also stated that if something is wrong or misleading, you can return it.

---

## Implementation
## Improvements
## Discussion
