from pink_morsel_visual import dash_app

def test_header_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout = 10)

def test_visualization_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout = 10)

def test_region_selector_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region-selector", timeout = 10)