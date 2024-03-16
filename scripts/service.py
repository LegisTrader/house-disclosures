import os
import logging
import time
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the PostgreSQL connection details from environment variables
db_host = os.environ.get('POSTGRES_HOST')
db_port = os.environ.get('OFFICIAL_DISCLOSURE_SERVICE_PORT_5432_TCP_ADDR')
db_name = os.environ.get('POSTGRES_DB')
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Create a session factory
Session = sessionmaker(bind=engine)

# Define the "legislators" table
metadata = MetaData()
legislators_table = Table('legislators', metadata, autoload_with=engine)

try:
    while True:
        # Create a session
        session = Session()

        try:
            # Execute a SELECT query to fetch random data from the "legislators" table
            random_legislator = session.execute(select([legislators_table]).order_by(func.random()).limit(1)).fetchone()
            logger.info(f'Random Legislator: {random_legislator}')

        except Exception as e:
            logger.error(f'Error executing query: {e}')

        finally:
            # Close the session
            session.close()

        # Sleep for 5 seconds
        time.sleep(5)

except Exception as e:
    logger.error(f'An error occurred: {e}')

finally:
    logger.info('Script execution completed')
