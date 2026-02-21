az login

az group create --name quantum-rg --location centralindia

az storage account create \
  --name quantumstorage123 \
  --resource-group quantum-rg \
  --location centralindia \
  --sku Standard_LRS

az storage container create \
  --name models \
  --account-name quantumstorage123

az appservice plan create \
  --name quantum-plan \
  --resource-group quantum-rg \
  --is-linux \
  --sku B1

az webapp create \
  --resource-group quantum-rg \
  --plan quantum-plan \
  --name quantum-plant-ai \
  --deployment-container-image-name <dockerhub-username>/quantum-plant:latest
