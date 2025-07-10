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

After that, you can visit the website at <a href="http://localhost:6969">http://localhost:6969/</a>

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

## Bonus:

### simulate-ai-insight endpoint

<b>Important:</b> for the simulate-ai-insight endpoint, you need a GOOGLE_API_KEY in a .env file, placed at the base of the project, at the same level than /backend and /frontend. This is the format of the .env file:

GOOGLE_API_KEY="abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcd"

After creating that file, run the make backend and make frontend in new terminals.

If you don't provide a valid google api key, that endpoint will show the message "Please provide a GOOGLE_API_KEY"

The google library may return the 503 error "The model is overloaded. Please try again later".

### Adding some more logging to backend

Now, the sorting api call prints a log:

```bash
logger.info(f"--------- Sort event: sort_options: {sort_options} ---------")
```

### Using environment variables to prepare the system for deployment on GCloud

I have created a yaml file (backend/cloudbuild.yaml) to deploy on GCloud:

```bash
gcloud builds submit --config=cloudbuild.yaml
```

On that file, I would have to put the name of the GCloud PROJECT_ID, etc. to successfully connect with my GCloud

### Basic frontend loading state and error display

I did that using useState to show some loaders and with Toast to show errors (and also the IA info about people and planets of Star Wars)
