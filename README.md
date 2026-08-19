# OpenShift AI 3.x Ansible

This Ansible Playbook provisions Red Hat OpenShift AI on an OpenShift Cluster in AWS.

## Preparation

### Order an OpenShift on AWS environment

On the [Red Hat Demo Platform](https://demo.redhat.com) order an [Red Hat OpenShift Container Platform Cluster (Multi-Cloud)](https://catalog.demo.redhat.com/catalog/all?item=babylon-catalog-prod%2Fpublished.ocp4-cluster.prod) environmment.

Once the cluster is provisioned you can get the following information from the **Red Hat Demo Platform**:

- OpenShift admin username and password
- OpenShift API URL

### Download Pull secret
Download a **Pull Secret** from [here](https://console.redhat.com/openshift/install/pull-secret) and place it into the current directory as ```pull_secret.json```.

### Configure Ansible

Get an offline token for Automation from [Connect to Hub](https://console.redhat.com/ansible/automation-hub/token).

Create an **ansible.cfg** file
```text
[galaxy]
server_list = published

[galaxy_server.published]
url=https://console.redhat.com/api/automation-hub/content/published/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<token>
```
Then execute
```bash
ansible-galaxy collection install ansible.controller
ansible-galaxy collection install kubernetes.core
ansible-galaxy collection install redhat.openshift
```
to install the ansible controller task.

Additional Python dependencies need to be installed:
```bash
pip install requests
pip install kubernetes
pip install dnspython
```
## Create vault
Create a file `group_vars/all/openshift.yaml` for the Openshift credentials and access details
```bash
admin: <admin>
password: <password>
api_url: <api URL>
base_domain: <base domain>
```
Now encrypt this file
```bash
ansible-vault encrypt group_vars/all/openshift.yaml
```
## Start Automation
To start the automation, run
```bash
ansible-playbook -vvv --ask-vault-pass -i inventory-ai.yaml playbook-ai-3.yaml 
```
