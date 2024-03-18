import os
import logging
import time
from sqlalchemy import create_engine, MetaData, Table, select, func
from sqlalchemy.orm import sessionmaker

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the PostgreSQL connection details from environment variables
db_host = os.environ.get('POSTGRES_HOST')
db_port = os.environ.get('POSTGRES_PORT')
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
    # Create a session
    session = Session()
    
    try:
        # Execute a SELECT * query to fetch all rows from the "legislators" table
        legislators = session.query(legislators_table).all()
        
        while True:
            # Select a random legislator from the fetched rows
            random_legislator = session.query(legislators_table).order_by(func.random()).limit(1).first()
            
            # Log the random legislator
            logger.info(f'Random Legislator: {random_legislator}')
            
            # Sleep for 5 seconds
            time.sleep(5)
    
    except Exception as e:
        logger.error(f'Error executing query: {e}')
    
    finally:
        # Close the session
        session.close()

except Exception as e:
    logger.error(f'An error occurred: {e}')

finally:
    logger.info('Script execution completed')