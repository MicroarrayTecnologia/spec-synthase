Spec-Synthase
=============
spec-synthase is a tool to help deal with big swagger files, by building the swagger specification file from small yaml files.

spec-synthase enables developers to reuse definitions and other swagger 2.0 spec pieces.

Supported Swagger 2.0 sections composition
******************************************
See `Swagger 2.0 Documentation <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md>`_ for reference.

Composable sections:

- definitions
- parameters
- paths
- responses
- securityDefinitions

Install
*******
**Install using pip:**

  ``pip install spec-synthase``

Command line interface
**********************
See `Spec-synthase examples <https://github.com/MicroarrayTecnologia/spec-synthase/tree/master/examples/specfiles>`_ for reference.

**Build PetStore API:**

``specsynthase pet_api.yaml petstore_definitions.yaml petstore_paths.yaml petstore_definitions_common.yaml > swagger.yaml``

**Build User API of PetStore:**

``specsynthase userapi/* > swagger.yaml``

**Build Store API of PetStore:**

``specsynthase userapi/* petstore_store_definitions.yaml petstore_store_paths.yaml > order_and_user.yaml``
