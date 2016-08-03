from flask_walrus import FlaskWalrus


def test_constructor_app(mocker):
    mocker.patch.object(FlaskWalrus, 'init_app', autospec=True)
    app_stub = mocker.stub(name='app_stub')

    FlaskWalrus(app_stub)

    FlaskWalrus.init_app.assert_called_once_with(mocker.ANY, app_stub)
