# pull official base image
FROM node:16.13.1-alpine3.12

# set work directory
WORKDIR /usr/src/app

RUN npm install -g npm@8.3.0

# copy our react project
COPY ./todo-app .

# npm install
RUN npm install

# perform npm build
RUN npm run build

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve
