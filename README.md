## Game Engine Project
This project is a custom-built game engine developed in Python. The primary goal of this endeavor is to demonstrate that while Python is often criticized for its performance limitations, it is fully capable of handling complex, per-frame calculations when designed with robust architectural patterns and rigorous optimization.

## Core Technologies & Architecture
### 1. Custom Entity Component System
To achieve high performance and readability, the engine moves away from traditional Object-Oriented design in favor of a custom Entity Component System.
### 2. AABB Tree Collision Detection
Collision detection is a notorious bottleneck in game engines. This project implements an Axis-Aligned Bounding Box Tree.<br>
The AABB tree allows for efficient collision detection, reducing the complexity of collision checks from $O(n^2)$ to $O(n \log n)$.<br>
This implementation ensures that even with a large number of active entities, the engine maintains a stable frame rate by only testing for collisions between potentially overlapping objects.
#### visualization: https://www.youtube.com/watch?v=UVObrDkek4g

## Why this project?
The common narrative suggests that Python is unsuitable for game development. This statement is true, however this engine serves as a proof-of-concept that it is more or less possible.

What I achieved:

- While working on the project, it was blatantly apparent why Python is not a suitable tool for game development. However, creating this project was really fun. 
- Efficient Algorithm Implementation: Demonstrates that using spatial acceleration structures can mitigate the performance cost of high-level languages.
- Effective Data Management: Shows how an ECS architecture allows Python to handle thousands of entities without falling into the object overhead trap.
- Scalability: Proves that with optimized Python code, one can perform complex, real-time spatial calculations per frame while maintaining a playable environment.

## What now?
I have prepared some examples of what the engine is capable of:

- top-down shooter: https://youtu.be/SlIkbh5IOqE?si=UI09qAFlXuKK1tvx
- platformer: https://youtu.be/xLigvF4lleI?si=b4f-DMhp0OFMwpnO
- grass: https://youtu.be/S3_GDXF9Amo?si=8v3kHquZAiuvq-Du
- grass-10k blades: https://youtu.be/-LsolTy1QPk?si=HVECxtyFi0fr141G
