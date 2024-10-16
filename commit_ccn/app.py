from flask import Flask
from .infraestructure.LizardCommitMetricsController import LizardCommitMetricsController

app = Flask(__name__)

# Registra los controladores (rutas) en la aplicación
app.register_blueprint(LizardCommitMetricsController)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
