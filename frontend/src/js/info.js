import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useEffect, useState } from 'react';

import * as API from './API/backendAPI';

function Info() {
  const [data,setData] = useState([]);
  const [update,setUpdate] = useState(false);

  const fetchData = async() => {
    const res = await API.getData()
    console.log(res)
    setData(res.data);
  }

  useEffect(() => {
    setInterval(() => setUpdate(update => !update),5000)
  },[])

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
          <Row className="fw-bold bg-light text-center" key={item.id}>
              <Col className="border">{item.name}</Col>
              <Col className="border">{item.state}</Col>
              <Col className="border">{item.in_time}</Col>
              <Col className="border">{item.out_time}</Col>
          </Row>
        ))}
      </div>
  );
}

export default Info;
