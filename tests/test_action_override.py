from sfdc_metadata_builder.models import action_overrides


def test_vfp_sfdc_classic():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <type>visualforce</type>
    <content>myEditVFPage</content>
    <comment>This edit action is a lot safer</comment>
</actionOverride>        
    """

    assert (
        action_overrides.ActionOverride().render(
            action_name="edit",
            type="visualforce",
            content="myEditVFPage",
            comment="This edit action is a lot safer",
        )
        == expected_output
    )

