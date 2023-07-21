import click
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper


@click.command()
@click.option('--input-schema', '-i', type=click.Path(exists=True), required=True)
@click.option('--output-schema', '-o', type=click.Path(), required=True)
def main(input_schema, output_schema):
    """
    Removes the `ExhaustiveTestClassCollection`, `ExhaustiveTestClass`, and `exhaustive_test_set`
    elements from a LinkML schema.
    """
    schema_view = SchemaView(input_schema, merge_imports=True)
    schema_schema = schema_view.schema
    schema_view.delete_slot()

    del schema_schema.classes['ExhaustiveTestClassCollection']
    del schema_schema.classes['ExhaustiveTestClass']
    del schema_schema.slots['exhaustive_test_set']

    yaml_dumper.dump(schema_schema, output_schema)


if __name__ == '__main__':
    main()
