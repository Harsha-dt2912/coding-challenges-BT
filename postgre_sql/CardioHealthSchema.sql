CREATE TABLE IF NOT EXISTS memberinfo (
    member_id VARCHAR(45) PRIMARY KEY,
    username VARCHAR(45),
    firstname VARCHAR(45),
    lastname VARCHAR(45),
    age INTEGER,
    gender VARCHAR(45),
    email VARCHAR(45),
    phonenumber BIGINT
);

CREATE TABLE IF NOT EXISTS addressinfo (
    address_id VARCHAR(45),
    city VARCHAR(45),
    state VARCHAR(45),
    country VARCHAR(45),
    pincode VARCHAR(45),
    memberinfo_member_id VARCHAR(45),
    PRIMARY KEY (address_id, memberinfo_member_id),
    CONSTRAINT fk_addressinfo_memberinfo
        FOREIGN KEY (memberinfo_member_id)
        REFERENCES memberinfo(member_id)
);

CREATE TABLE IF NOT EXISTS cardiodiagnosis (
    cardio_id VARCHAR(45),
    cardioarrestdetected INTEGER,
    date TIMESTAMP,
    memberinfo_member_id VARCHAR(45),
    PRIMARY KEY (cardio_id, memberinfo_member_id),
    CONSTRAINT fk_cardiodiagnosis_memberinfo
        FOREIGN KEY (memberinfo_member_id)
        REFERENCES memberinfo(member_id)
);

ALTER TABLE cardiodiagnosis
ADD CONSTRAINT uq_cardiodiagnosis_cardio_id UNIQUE (cardio_id);

CREATE TABLE IF NOT EXISTS bloodtest (
    blood_id VARCHAR(45),
    date TIMESTAMP,
    bloodpressure INTEGER,
    fbs INTEGER,
    thal INTEGER,
    serumcholesterol INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (blood_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_bloodtest_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE IF NOT EXISTS diseasedetail (
    disease_id VARCHAR(45),
    diagnoseddate TIMESTAMP,
    recovereddate TIMESTAMP,
    isrecovered BOOLEAN,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (disease_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_diseasedetail_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE IF NOT EXISTS ecgreport (
    ecg_id VARCHAR(45),
    date TIMESTAMP,
    restecg INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (ecg_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_ecgreport_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE IF NOT EXISTS symptom (
    symptom_id VARCHAR(45),
    date TIMESTAMP,
    exang INTEGER,
    oldpeak REAL,
    cp INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (symptom_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_symptom_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE IF NOT EXISTS wearabledevicedata (
    wearable_device_id VARCHAR(45),
    thalach INTEGER,
    slope INTEGER,
    date TIMESTAMP,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (wearable_device_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_wearabledevicedata_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE IF NOT EXISTS xray (
    xray_id VARCHAR(45),
    date TIMESTAMP,
    ca INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (xray_id, cardiodiagnosis_cardio_id),
    CONSTRAINT fk_xray_cardiodiagnosis
        FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);
