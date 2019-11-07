# Azure Functions

Testing with Azure functions.

* **queue-trigger-blob-in-out-binding**

> OBS: To connect KV and App Functions securely via specific policies, we need to enable the Identity of the Azure Function. The idea is that we are registering this resource with AAD. After that, we can add an Access Policy in KV with the Service Principal as the Azure Function name. Finally, in the App Function, add a value with content the *Secret Identifier* URL.

> OBS: When using queue triggers, if a message has not been successfuly processed, a *poison* queue is automatically created to store it.

# Credits

* Great [repo](https://github.com/yokawasa/azure-functions-python-samples) with examples.
* Securing Azure Functions [post](https://daniel-krzyczkowski.github.io/Integrate-Key-Vault-Secrets-With-Azure-Functions/).
* Unit Testing [docs](https://docs.microsoft.com/bs-latn-ba/azure/azure-functions/functions-reference-python#unit-testing).

