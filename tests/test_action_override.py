from sfdc_metadata_builder.models import action_overrides


def test_vfp_sfdc_classic():
    expected_output = """
<actionOverride>
    <actionName>edit</actionName>
    <comment>This edit action is a lot safer.</comment>
    <content>myEditVFPage</content>
    <type>visualforce</type>
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
    <comment>This edit action is a lot safer.</comment>
    <content>myEditLightningComponent</content>
    <formFactor>Large</formFactor>
    <type>lightningcompenent</type>
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
    <content>myEditLightingComponent</content>
    <formFactor>Small</formFactor>
    <type>lightningcomponent</type>
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


def test_lightning_page_action_override():
    expected_output = """
<actionOverride>
    <actionName>view</actionName>
    <content>myLightningPage</content>
    <formFactor>Large</formFactor>
    <type>flexipage</type>
</actionOverride>
    """
    assert (
        action_overrides.ActionOverride(
            action_name="view",
            content="myLightningPage",
            form_factor="Large",
            type="flexipage",
        ).render()
        == expected_output
    )
