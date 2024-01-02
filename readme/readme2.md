
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/": {
            "get": {
                "summary": "Get Index Html",
                "operationId": "get_index_html__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                }
            }
        },
        "/percentage": {
            "get": {
                "summary": "Get Random Percentage",
                "operationId": "get_random_percentage_percentage_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                }
            }
        },
        "/users": {
            "get": {
                "summary": "Read Users",
                "operationId": "read_users_users_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/User"
                                    },
                                    "type": "array",
                                    "title": "Response Read Users Users Get"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Register User",
                "operationId": "register_user_users_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/UserCreate"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user_id}": {
            "get": {
                "summary": "Read User",
                "operationId": "read_user_users__user_id__get",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "title": "User Id"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "summary": "Remove User",
                "operationId": "remove_user_users__user_id__delete",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "title": "User Id"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "summary": "Update Existing User",
                "operationId": "update_existing_user_users__user_id__put",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "title": "User Id"
                        }
                    }
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/UserUpdate"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/users/{user_id}/items/": {
            "post": {
                "summary": "Create Item For User",
                "operationId": "create_item_for_user_users__user_id__items__post",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "integer",
                            "title": "User Id"
                        }
                    }
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/ItemCreate"
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Item"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/items/": {
            "get": {
                "summary": "Read Items",
                "operationId": "read_items_items__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/Item"
                                    },
                                    "type": "array",
                                    "title": "Response Read Items Items  Get"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/bands": {
            "get": {
                "summary": "Read Bands",
                "operationId": "read_bands_bands_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/Band"
                                    },
                                    "type": "array",
                                    "title": "Response Read Bands Bands Get"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Create Band Endpoint",
                "operationId": "create_band_endpoint_bands_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/BandCreate"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "201": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Band"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/festivals": {
            "get": {
                "summary": "Read Festivals",
                "operationId": "read_festivals_festivals_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/Festival"
                                    },
                                    "type": "array",
                                    "title": "Response Read Festivals Festivals Get"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Create Festivals Endpoint",
                "operationId": "create_festivals_endpoint_festivals_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/FestivalCreate"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "201": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Festival"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/poduims": {
            "get": {
                "summary": "Read Poduims",
                "operationId": "read_poduims_poduims_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "items": {
                                        "$ref": "#/components/schemas/Podium"
                                    },
                                    "type": "array",
                                    "title": "Response Read Poduims Poduims Get"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Create Poduims Endpoint",
                "operationId": "create_poduims_endpoint_poduims_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/PodiumCreate"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "201": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Podium"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "Band": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    },
                    "id": {
                        "type": "string",
                        "format": "uuid",
                        "title": "Id"
                    }
                },
                "type": "object",
                "required": [
                    "name",
                    "id"
                ],
                "title": "Band"
            },
            "BandCreate": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    }
                },
                "type": "object",
                "required": [
                    "name"
                ],
                "title": "BandCreate"
            },
            "Festival": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    },
                    "location": {
                        "type": "string",
                        "title": "Location"
                    },
                    "price": {
                        "type": "number",
                        "title": "Price"
                    },
                    "year": {
                        "type": "integer",
                        "title": "Year"
                    },
                    "id": {
                        "type": "string",
                        "format": "uuid",
                        "title": "Id"
                    }
                },
                "type": "object",
                "required": [
                    "name",
                    "location",
                    "price",
                    "year",
                    "id"
                ],
                "title": "Festival"
            },
            "FestivalCreate": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    },
                    "location": {
                        "type": "string",
                        "title": "Location"
                    },
                    "price": {
                        "type": "number",
                        "title": "Price"
                    },
                    "year": {
                        "type": "integer",
                        "title": "Year"
                    }
                },
                "type": "object",
                "required": [
                    "name",
                    "location",
                    "price",
                    "year"
                ],
                "title": "FestivalCreate"
            },
            "HTTPValidationError": {
                "properties": {
                    "detail": {
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        },
                        "type": "array",
                        "title": "Detail"
                    }
                },
                "type": "object",
                "title": "HTTPValidationError"
            },
            "Item": {
                "properties": {
                    "title": {
                        "type": "string",
                        "title": "Title"
                    },
                    "description": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "Description"
                    },
                    "id": {
                        "type": "string",
                        "format": "uuid",
                        "title": "Id"
                    },
                    "owner_id": {
                        "type": "string",
                        "title": "Owner Id"
                    }
                },
                "type": "object",
                "required": [
                    "title",
                    "description",
                    "id",
                    "owner_id"
                ],
                "title": "Item"
            },
            "ItemCreate": {
                "properties": {
                    "title": {
                        "type": "string",
                        "title": "Title"
                    },
                    "description": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "Description"
                    }
                },
                "type": "object",
                "required": [
                    "title"
                ],
                "title": "ItemCreate"
            },
            "Podium": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    },
                    "podium_id": {
                        "type": "string",
                        "title": "Podium Id"
                    }
                },
                "type": "object",
                "required": [
                    "name",
                    "podium_id"
                ],
                "title": "Podium"
            },
            "PodiumCreate": {
                "properties": {
                    "name": {
                        "type": "string",
                        "title": "Name"
                    }
                },
                "type": "object",
                "required": [
                    "name"
                ],
                "title": "PodiumCreate"
            },
            "User": {
                "properties": {
                    "first_name": {
                        "type": "string",
                        "title": "First Name"
                    },
                    "last_name": {
                        "type": "string",
                        "title": "Last Name"
                    },
                    "email": {
                        "type": "string",
                        "title": "Email"
                    },
                    "id": {
                        "type": "string",
                        "format": "uuid",
                        "title": "Id"
                    },
                    "is_active": {
                        "type": "boolean",
                        "title": "Is Active"
                    },
                    "items": {
                        "items": {
                            "$ref": "#/components/schemas/Item"
                        },
                        "type": "array",
                        "title": "Items",
                        "default": []
                    }
                },
                "type": "object",
                "required": [
                    "first_name",
                    "last_name",
                    "email",
                    "id",
                    "is_active",
                    "items"
                ],
                "title": "User"
            },
            "UserCreate": {
                "properties": {
                    "first_name": {
                        "type": "string",
                        "title": "First Name"
                    },
                    "last_name": {
                        "type": "string",
                        "title": "Last Name"
                    },
                    "email": {
                        "type": "string",
                        "title": "Email"
                    },
                    "password": {
                        "type": "string",
                        "title": "Password"
                    }
                },
                "type": "object",
                "required": [
                    "first_name",
                    "last_name",
                    "email",
                    "password"
                ],
                "title": "UserCreate"
            },
            "UserUpdate": {
                "properties": {
                    "first_name": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "First Name"
                    },
                    "last_name": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "Last Name"
                    },
                    "email": {
                        "anyOf": [
                            {
                                "type": "string"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "Email"
                    }
                },
                "type": "object",
                "required": [
                    "first_name",
                    "last_name",
                    "email"
                ],
                "title": "UserUpdate"
            },
            "ValidationError": {
                "properties": {
                    "loc": {
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "type": "array",
                        "title": "Location"
                    },
                    "msg": {
                        "type": "string",
                        "title": "Message"
                    },
                    "type": {
                        "type": "string",
                        "title": "Error Type"
                    }
                },
                "type": "object",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "title": "ValidationError"
            }
        }
    }
}