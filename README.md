<div>
    <h1 align="center">:dart: SRE Playground</h1>
<p align="center">The goal of this project is to introduce you to basic SRE topics. It was designed to give an overview covered by SRE during a whole application life-cycle. </p>
</div>

## :book: Walkthrough
We will divide this challenge into multiple stages to more closely explain what is happening in each cycle.     

- [:thought_balloon: Design](#thought_balloon-design)
    - [*What is the tech-stack?*](#grey_question-what-is-the-tech-stack)
    - [*How does it work?*](#grey_question-how-does-it-work)
    - [*When, and how often?*](#grey_question-when-and-how-often)
    - [*Should you know this?*](#grey_question-should-you-know-this)
    - [*What if?*](#grey_question-what-if)
    - [*What is happening?*](#grey_question-what-is-happening)
    - [*How good is all this?*](#grey_question-how-good-is-all-this)
- [:computer: Implementation](#computer-implementation)
    - [Architecture overview](#architecture-overview)
    - [Infrastructure specifications](#infrastructure-specifications)
- [:checkered_flag: Challenges](#checkered_flag-challenges)
    - [Code submission](#warning-code-submission)
    - [Scoring](#memo-scoring)
- [:star: Further references](#star-further-references)

## :thought_balloon: Design
Start by thinking about how the whole infrastructure can be deployed, maintained, monitored, discarded, extended, or automated. The point of this step is to have a clearer picture of how to proceed, to rule out all the improbable scenarios and major blockers. In this step, try to answer some basic architectural and support questions.   

---

#### :grey_question: *What is the tech-stack?*
It will give you an idea of what technologies you as an SRE should continue with. Remember, you are defining the way how the whole process is going to work. Hence, you need to decide on the tools you are going to be working with.      
     
#### :grey_question: *How does it work?*
Get a nice overview of how the solution works. Usually, here you get a lot of graphs, or you need to create them. Graphs help you get a grasp of what is happening. Some services talk to each other, some are independent, some require more memory, some require a lot of computing power. Here you need information - **well-defined** and **concise** **information**. Without understanding what is happening, you cannot decide what you want to happen.     
 
#### :grey_question: *When, and how often?*
Here, you need to think in terms of how the whole solution is going to be updated, deleted, recreated, or moved. Most likely, you will have to implement some kind of automated mechanism on how to combat these issues. Notoriously, this is the moment when **Continuous Integration (CI)**, **Continuous Deployment (CD)**, **Anything-as-a-Code (XaaS)**  comes into the picture. They are not your enemy!     

#### :grey_question: *Should you know this?*
One of the big challenges of automation is knowing how to secure your things. When you are developing, you want to isolate the parts that require authorization from the public, and once it has been created, glue it inside of the bigger part without allowing anyone to know how the process had been achieved. In this scenario, you have to integrate the **Secret** controlling mechanisms to strip away all the required private data from the service logic.   
     
#### :grey_question: *What if?*
If you want the solution to be bullet-proof, you have to take into account on how everything is going to behave once It is up and running. These are referred to as **edge-cases**, and a proper solution has to cover them. Your infrastructure is built to serve US West Coast under 100ms, but what do you do for connections from India? It is Black Friday, and suddenly you have 100x higher traffic than usual. Typically, this has to do something with **auto-scaling**, **load balancing**, or **networking**. Your task is now to think of any impossible case scenario in which your infrastructure will fail -- and extend to support it.    
     
#### :grey_question: *What is happening?*
A question you will often ask throughout the whole process. Everything is now operational, you have come this far. But, one of the services is down (perhaps, a like button on Facebook is not counting likes properly), and you don't know what to do. Here, you need to set up the **Monitoring**, **Logging**, and **Observability** services. They help you troubleshoot and see what is happening in realtime. They spew out a lot of unnecessary things, so correctly configuring them will help you manage everything more easily.       
     
#### :grey_question: *How good is all this?*
Whenever you are building something, you need to know how well it behaves. This part is focused on answering how your infrastructure is doing, health and functional -wise. It is commonly referred to as **Service Level Agreement (SLA)** which works based on **Service Level Indicators (SLI)**. They depict legal requirements and arrangements between a user and the service provider.     

---

## :computer: Example real-world example

### Architecture overview
![Architecture Diagram](diagram.png)

| Service | Model | Networking Type | Port | Paths | Response time | Dependencies | Extras
|---|---|---|---|---|---|---|---|
| **data** | container | Internal | 9876 | /api/* | < 200ms | | |
| **info** | container | Internal | 5555 | /* | < 50ms | data | | |
| **load balancer** | platform supported  | External | 80, 443 | / | | info | |
| **monitoring** | optional | | | | | | |

### Infrastructure specifications
| Service | Rate of change (weekly) | Versioning (optional) | Details | Rollout strategy (optional) | Type |
|---|---|---|---|---|---|
| **infrastructure** | 5 | Yes | | A/B Deployment | IaaC |
| **load balancer** | 1-2 | No | Should be part of infrastructure code, but supported separately. | Big Bang Deployment | IaaC |
| **data** | > 50 | Yes | Storage must not be discarded. Keep logs. Enhance security rules. Reconfigure path rules before swapping with the old version. | Rolling Deployment | SaaC |
| **info** | > 50 | Yes | Must support high availability. | Rolling Deployment | SaaC |
| **monitoring** | 1-2 | Yes | Ensure firewall rules, authentication, and authorization. Support only internal networks. | Rolling Deployment | SaaC |

We would also like to have a way of knowing when the deployments fail or succeed. Find a way to notify the users working on the project about the deployment statuses.

### Service specifications
This can contain everything regarding a service (e.g. resource requirements, availability,...).

## :checkered_flag: Challenges
An example approach to solving such a challenge could be summarized briefly in the following steps:

1) **Containerization** - Write Dockerfiles for data and info services.
2) **Environment preparation** - Register a [Google Cloud Platform](https://cloud.google.com/free) free tier account, and create a GCP project.
3) **Configuration** - Create a GCP service account that has read and write permissions to the Google Cloud Registry. Set Registry rules to private. Authenticate your service account against Docker.
4) **Basic CI** - Select an appropriate Continuous Integration tool for your project (refer to [Wiki: Comparison of continuous integration software](https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software) for more details). Your pipeline should be either manually or push triggered, and should only consist of a step that builds docker images for data and info services. Leave some room for extending the pipeline.
5) **(optional) Pipeline as a Code** - Configure your Pipeline strategy to be code manageable. This step includes configuring the appropriate repo which will serve as a base for extending the pipeline. Reefer to [Pipeline as Code with Jenkins](https://jenkins.io/solutions/pipeline/) for details on how you can utilize Jenkins for this task.
6) **Tests** - Write some basic tests to check the functionality of the services. Add the testing stage to your CI pipeline.
7) **Extending CI pipeline** - Extend your CI pipeline to push the built docker images to Google Cloud Registry. In this step, find a way to use secrets when pushing the images to the repo.
8) **Extending CD pipeline** - Write a docker-compose file that deploys two services into a service mesh. Be sure to mount the appropriate ports to appropriate services.
9) **Environment-all** - Update the Python services to use Environment variables instead of hard-coded values. This step will be important (more technically, we will use environment variables when configuring the rollout strategies and mostly abuse them for infrastructure configurations).
10) **Hyperscalers** - Create an instance within your Google Cloud Project. Create a service account within GCP that has read/write access to your instance, and save it. We will use an instance for deploying Docker compose service.
11) **(optional) Infrastructurization** - Familiarize yourself with IaaS tools. Write an IaaC solution that will automatically create a GKE Cluster for you. Reefer to [the-ultimate-devops-tool-chest](https://xebialabs.com/the-ultimate-devops-tool-chest/#tool-chest-type) to select appropriate tools (Authors suggestion: Terraform).
12) **(optional) Kubernetization** - Create Kubernetes deployment scripts for your services.
> *More challenges will be added...* - Author

## :memo: Example evaluation
Every implementation will be scored based on the criteria below.

* Automation
* Security
* Monitoring
* Logging
* Scalability
* Extendability

## :star: Further references
Visit [Awesome Site Reliability Engineering](https://github.com/dastergon/awesome-sre/blob/master/README.md) to find major information about most of the SRE related topics.

---
