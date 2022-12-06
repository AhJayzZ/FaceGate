import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/esm/Button';
import { useEffect, useState } from 'react';

import * as API from './API/backendAPI';

function Info() {
  const [data,setData] = useState([]);
  const [update,setUpdate] = useState(false);


  const fetchData = async() => {
    const res = await API.getData()
    setData(res.data);
  }
  
  const deleteData = async(id) => {
      await API.deleteData(id);
      setUpdate(update => !update);
  }

  useEffect(() => {
    fetchData();
  },[update]);

  return (
      <div>
        <br />
        <Row className="text-white bg-primary fw-bold text-center">
            <Col>人員</Col>
            <Col>狀態</Col>
            <Col>進入時間</Col>
            <Col>離開時間</Col>
            <Col>刪除資料</Col>
        </Row>
        {data.map(item => (
          <Row className="fw-bold bg-light" key={item.id}>
              <Col className="border">{item.name}</Col>
              <Col className="border">{item.status}</Col>
              <Col className="border">{item.entryTime}</Col>
              <Col className="border">{item.departureTime}</Col>
              <Col className="border text-center">
                <Button variant='danger' onClick={ ()=> deleteData(item.id)}>刪除</Button>
              </Col>
          </Row>
        ))}
      </div>
  );
}

export default Info;
