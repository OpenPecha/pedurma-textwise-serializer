<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

<h3 align="center">OpenPecha Toolkit</h3>

<!-- Replace the title of the repository -->

<p align="center">
  <a href="#description">Description</a> •
  <a href="#owner">Owner</a> •
  <a href="#floppy_disk-install">Install</a> •
  <a href="#docs">Docs</a>
</p>
<hr>

## Description

[![PyPI version](https://badge.fury.io/py/openpecha.svg)](https://badge.fury.io/py/openpecha)
[![Test](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/test.yml/badge.svg)](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/test.yml)
[![Test Coverage](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/test-coverage.yaml/badge.svg)](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/test-coverage.yaml)
[![Publish](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/publish.yaml/badge.svg)](https://github.com/OpenPecha-dev/openpecha-toolkit/actions/workflows/publish.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repo contains two opfs of pedurma tengyur. The pecha id 12d32eb31c1a4cc59741cda99ebc7211.opf is pedurma opf with derge base and google ocred base. The pecha id 187ed94f85154ea5b1ac374a651e1770.opf is pedurma opf with namsel ocred base. The script textwise serializer will serialize text from the opf.

<!-- This section provides a high-level overview for the repo -->

## Owner

- [@kaldan007](https://github.com/kaldan007)

<!-- This section lists the owners of the repo -->




<!-- This section must list as bulleted list how this repo depends or is integrated with other repos -->

## Docs

Steps that we have gone through preparing the opfs are as follow:

- we have ocred the pedurma and format it in opf

- we parse the bdrc outline to get image number range of the texts, pg number range of texts, title, durchen page and image range

- we parsed title and text Id from rkts outline 

- using the image number info of outlines and pagination layers, we tried to reconstruct the index of pedurma

- using the same info we annotated the durchen starting point and ending point

- after that we have serialize the annotations in html(human friendly markup language) 

- given them to our freelancer to manually check the actual table of content

- reformat the updated hfmls to opf

** Regarding the derge Google pedurma, we have transfer all the base text to Google ocred opf base and updated all the layers. But we have left the volumes which are not in derge as it as in the opf
