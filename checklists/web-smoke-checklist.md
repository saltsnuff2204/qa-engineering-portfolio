# Web Smoke Checklist

## Environment

- [ ] Backend starts without exposing credentials or stack traces
- [ ] `GET /api/health` returns `200 OK`
- [ ] Frontend starts and loads without blocking console errors
- [ ] Database connection uses a dedicated test account

## Core flow

- [ ] Menu list loads
- [ ] Empty menu state is readable
- [ ] Valid dish can be created
- [ ] Valid drink can be created
- [ ] Search returns the expected item
- [ ] Category filter narrows results correctly
- [ ] Delete confirmation appears
- [ ] Confirmed deletion removes the intended item
- [ ] Cancelled deletion leaves data unchanged

## Validation and failure handling

- [ ] Blank name is rejected
- [ ] Zero and negative prices are rejected
- [ ] Invalid JSON receives a safe `400` response
- [ ] Missing item deletion receives `404`
- [ ] API outage displays a clear UI error
- [ ] No secret, SQL error, or stack trace appears in the browser response

## UI and compatibility

- [ ] Keyboard focus reaches all interactive controls
- [ ] Labels and validation messages are understandable
- [ ] Current Chrome desktop flow passes
- [ ] Mobile viewport has no overlapping controls
- [ ] Table remains usable on a narrow screen

