import React, { useState } from "react";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Engine from "./Engine";
const Dashboard = () => {
  const [key, setKey] = useState("home");
  return (
    <Container fluid style={{ paddingTop: "70px" }}>
      <Row>
        <Col xs={1}></Col>
        <Col xs={10}>
          {" "}
          <Tabs
            id="controlled-tab-example"
            activeKey={key}
            onSelect={(k) => setKey(k)}
            className="mb-3"
          >
            <Tab eventKey="home" title="Suggestion Engine">
              <Engine />
            </Tab>

            <Tab eventKey="profile" title="View Portfolios"></Tab>
          </Tabs>
        </Col>
        <Col xs={1}></Col>
      </Row>
    </Container>
  );
};

export default Dashboard;
