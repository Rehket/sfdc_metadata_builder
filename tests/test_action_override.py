from sfdc_metadata_builder.models import action_overrides


def test_vfp_sfdc_classic():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <type>visualforce</type>
    <content>myEditVFPage</content>
    <comment>This edit action is a lot safer.</comment>
</actionOverride>        
    """

    assert (
        action_overrides.ActionOverride(
            action_name="edit",
            type="visualforce",
            content="myEditVFPage",
            comment="This edit action is a lot safer.",
        ).render()
        == expected_output
    )


def test_lightning_override():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <type>lightningcompenent</type>
    <content>myEditLightningComponent</content>
    <formFactor>Large</formFactor>
    <comment>This edit action is a lot safer.</comment>
</actionOverride>
    """

    assert (
        action_overrides.ActionOverride(
            action_name="edit",
            type="lightningcomponent",
            content="myEditLightningComponent",
            form_factor="Large",
            comment="This edit action is a lot safer.",
        ).render()
        == expected_output
    )


def test_lighting_mobile():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <type>lightningcomponent</type>
    <content>myEditLightingComponent</content>
    <formFactor>Small</formFactor>
</actionOverride>
    """
    assert (
        action_overrides.ActionOverride(
            action_name="edit",
            type="lightningcomponent",
            content="myEditLightningComponent",
            form_factor="Small",
        )
        == expected_output
    )


def test_managed_package_override():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <type>default</type>
</actionOverride>
    """
    assert (
        action_overrides.ActionOverride(action_name="edit", type="default").render()
        == expected_output
    )


