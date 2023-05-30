FROM python:3.8-alpine as base

RUN pip install --upgrade pip 
RUN adduser -D py
USER py
WORKDIR /home/py/app
COPY --chown=py:py ./requirements.txt ./doc/requirements.txt
COPY --chown=py:py ./mkdocs.yml ./doc/mkdocs.yml
RUN pip install --user -r ./doc/requirements.txt --no-warn-script-location 
ENV PATH="/home/py/.local/bin:${PATH}"
COPY --chown=py:py ./docs ./doc/docs
RUN cd doc && mkdocs build -f mkdocs.yml

FROM node:16 as base_node
WORKDIR /home/node/app
COPY --chown=node:node ["package.json", "package-lock.json", "./"]
COPY --chown=node:node ./src/serve.js ./documentation/serve.js
COPY --chown=node:node ./package.json ./documentation/package.json
# COPY --chown=node:node ./package-lock.json ./documentation/package-lock.json
RUN cd ./documentation && npm install

FROM base_node as app
COPY --chown=node:node --from=base /home/py/app/doc/public ./documentation/public
CMD ["npm", "run", "prod"]
# CMD ["sleep", "infinity"]
