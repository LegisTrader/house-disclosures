# Official Disclosure Service

This repository contains the deployment configurations for the Official Disclosure Service, a Helm chart for Kubernetes.

## Overview

The Official Disclosure Service is designed to iterate through a list of US representatives and check for newly disclosed stock trades. The list it iterates through is created and maintained by a separate microservice that can be found here [Officials List Microservice](https://github.com/Travbz/officials-list). It is currently a work in progress.

## Prerequisites

Before deploying the service, ensure the following prerequisites are met:

- Kubernetes cluster is set up and accessible.
- Helm 3 is installed.
