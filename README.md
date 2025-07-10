# A New Dawn

!["Do. Or do not. There is no try." - Yoda](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmJubnA3czEyYWlqYnpvYmlqMWtpaXdneWpyaDR0bWF4bGFhajFhayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26FmQ6EOvLxp6cWyY/giphy.gif)

## Overview

I am using <b>hexagonal architecture</b> design for the "in" part, where the data from the external api flows into my api. The "out" part is very simple (it connects to the simple frontend) and doesn't need that configuration.

## How to run the project

First, clone the repository and navigate into the project directory. Then, you can create the docker images and run the containers with these commands:

```bash
make backend
make frontend
```
After that, you can visit the website at <a href="http://stackoverflow.com">http://localhost:6969/</a>

### How to run the backend tests

```bash
make unit
make integration
```

### How to run the frontend tests

```bash
cd frontend
npm test
```
