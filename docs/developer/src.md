# Source Code Structure

```
python-notion-mbse/
├── api/
│   ├── controllers/
│   │   ├── elementController.py
│   │   ├── viewpointController.py
│   │   ├── relationController.py
│   │   └── validationController.py
│   ├── models/
│   │   ├── elementModel.py
│   │   ├── viewpointModel.py
│   │   ├── relationModel.py
│   │   └── oclConstraintModel.py
│   ├── routes/
│   │   ├── elementRoutes.py
│   │   ├── viewpointRoutes.py
│   │   ├── relationRoutes.py
│   │   └── validationRoutes.py
│   ├── services/
│   │   ├── elementService.py
│   │   ├── viewpointService.py
│   │   ├── relationService.py
│   │   ├── validationService.py
│   │   └── oclInterpreter.py
│   ├── utils/
│   │   ├── db.py
│   │   ├── notionIntegration.py
│   │   ├── milvusIntegration.py
│   │   └── oclUtils.py
│   └── app.py
├── cli/
│   ├── commands/
│   │   ├── initCommand.py
│   │   ├── configCommand.py
│   │   ├── createCommand.py
│   │   ├── linkCommand.py
│   │   ├── fetchCommand.py
│   │   ├── syncCommand.py
│   │   ├── validateCommand.py
│   │   ├── exportCommand.py
│   │   ├── importCommand.py
│   │   ├── reportCommand.py
│   │   ├── shareCommand.py
│   │   ├── backupCommand.py
│   │   ├── restoreCommand.py
│   │   ├── logCommand.py
│   │   └── customizeCommand.py
│   └── cli.py
├── db/
│   ├── mongo/
│   │   └── initMongo.py
│   ├── milvus/
│   │   └── initMilvus.py
│   └── migrations/
│       └── migrationScripts.py
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── docs/
│   ├── API.md
│   ├── CLI.md
│   ├── setup.md
│   ├── architecture.md
│   ├── validation.md
│   └── contributing.md
├── tests/
│   ├── api/
│   │   ├── test_element.py
│   │   ├── test_viewpoint.py
│   │   ├── test_relation.py
│   │   └── test_validation.py
│   ├── cli/
│   │   ├── test_init.py
│   │   ├── test_config.py
│   │   ├── test_create.py
│   │   ├── test_link.py
│   │   ├── test_fetch.py
│   │   ├── test_sync.py
│   │   ├── test_validate.py
│   │   ├── test_export.py
│   │   ├── test_import.py
│   │   ├── test_report.py
│   │   ├── test_share.py
│   │   ├── test_backup.py
│   │   ├── test_restore.py
│   │   ├── test_log.py
│   │   └── test_customize.py
│   └── db/
│       ├── test_mongo.py
│       └── test_milvus.py
├── .env
├── README.md
└── setup.py
```

```text
src/notion_mbse
├── controllers
│   ├── base_controller.py
│   ├── control_element.py
│   ├── controllers.py
│   └── __init__.py
├── __init__.py
├── __main__.py
├── managers
├── models
│   ├── document.py
│   ├── element.py
│   ├── __init__.py
│   └── notion.py
├── ui
│   └── cli.py
└── utils
    ├── etl.py
    ├── notion_db.py
    └── omg.py
```
